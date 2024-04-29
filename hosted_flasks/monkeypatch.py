import logging

from collections import UserDict

from pathlib import Path

import inspect

import os

from hosted_flasks import loader

logger = logging.getLogger(__name__)

# os.environ.get

class Environment(UserDict):

  def __init__(self, *args, **kwargs):
    self._debug = False
    super().__init__(*args, **kwargs)

  def _get_raw(self, key):
    # utility to access env var without looking up the calling app
    return super().__getitem__(key)  # pragma: no cover

  def _log(self, msg):
    if self._debug:
      logger.info(msg) # pragma: no cover

  def _get_calling_app(self):
    # walk up the stack to find a frame that originated in one of the hosted
    # flasks. if so, use its name as a prefix for retrieving an app specific
    # version of the environment variable
    frames = inspect.stack()[2:]
    for caller in frames:
      self._log(f"matching {caller.filename}")
      for app in loader.apps: # access apps directly to avoid loop with get_apps
        try:
          self._log(f"  against {app.src.parent}")
          calling_app = Path(caller.filename).relative_to(app.src.parent).parts[0]
          # we found a frame that originated in a hosted flask app's src
          # the root of this path is the app folder and also the prefix name
          self._log(f"  SUCCESS: {calling_app}")
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

  def __getitem__(self, key):
    # in case of a call from a hosted flask app, try a prefix first
    calling_app = self._get_calling_app()
    if calling_app:
      app_key = f"{calling_app.upper()}_{key}"
      self._log(f"  trying to get {app_key}")
      try:
        value = super().__getitem__(app_key)
        self._log(f"  SUCCESS {app_key} = {value}")
        return value
      except KeyError:
        pass

    # fall back to the non-prefixed variable
    self._log(f"  FAIL: trying {key}")
    try:
      value = super().__getitem__(key)
    except KeyError:
      raise KeyError

    return value

os.environ = Environment(os.environ)
