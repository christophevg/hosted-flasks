from collections import UserDict

from pathlib import Path

import inspect

import os

from hosted_flasks.loader import apps

# os.environ.get

class Environment(UserDict):
  def get(self, key, default=None):
    # walk up the stack to find a frame that originated in one of the hosted
    # flasks. if so, use its name as a prefix for retrieving an app specific
    # version of the environment variable
    for index, caller in enumerate(inspect.stack()[1:]):
      for app in apps:
        try:
          calling_app = Path(caller.filename).relative_to(app.src.parent).parts[0]
          # we found a frame that originated in a hosted flask app
          # the root of this path is the app folder and also the prefix name
          app_key = f"{calling_app.upper()}_{key}"
          value = super().get(app_key, None)
          if value:
            return value
        except ValueError: # pathlib: does not start with...
          pass

    # fall back to the non-prefixed variable
    return super().get(key, default)

os.environ = Environment(os.environ)
