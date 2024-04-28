from collections import UserDict

from pathlib import Path

import inspect

import os

from hosted_flasks import loader

# os.environ.get

class Environment(UserDict):

  def _get_calling_app(self):
    # walk up the stack to find a frame that originated in one of the hosted
    # flasks. if so, use its name as a prefix for retrieving an app specific
    # version of the environment variable
    for index, caller in enumerate(inspect.stack()[1:]):
      for app in loader.apps: # access apps directly to avoid loop with get_apps
        try:
          calling_app = Path(caller.filename).relative_to(app.src.parent).parts[0]
          # we found a frame that originated in a hosted flask app's src
          # the root of this path is the app folder and also the prefix name
          return calling_app
        except ValueError: # pathlib: does not start with...
          pass
    return None
  
  def __setitem__(self, key, value):
    # in case of a call from a hosted flask app, add a prefix
    calling_app = self._get_calling_app()
    if calling_app:
      key = f"{calling_app.upper()}_{key}"
    super().__setitem__(key, value)

  def get(self, key, default=None):
    # in case of a call from a hosted flask app, try a prefix first
    calling_app = self._get_calling_app()
    if calling_app:
      app_key = f"{calling_app.upper()}_{key}"
      value = super().get(app_key, None)
      if value:
        return value

    # fall back to the non-prefixed variable
    return super().get(key, default)

os.environ = Environment(os.environ)
