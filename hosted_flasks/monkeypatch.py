from collections import UserDict

from pathlib import Path

import inspect

import os

from hosted_flasks import config

# os.environ.get

class Environment(UserDict):
  def get(self, key, default=None):
    # walk up the stack to find a frame that originated in one of the hosted
    # flasks. if so, use its name as a prefix for retrieving an app specific
    # version of the environment variable
    for caller in inspect.stack()[1:]:
      try:
        app = Path(caller.filename).relative_to(config.apps_folder).parts[0]
        # we found a frame that originated in a hosted flask app
        # the root of this path is the app folder and also the prefix name
        value = super().get(f"{app.upper()}_{key}", None)
        if value:
          return value
      except ValueError: # pathlib: does not start with...
        pass

    # fall back to the non-prefixed variable
    return super().get(key, default)

os.environ = Environment(os.environ)
