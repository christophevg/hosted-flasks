__version__ = "0.0.4"

# ruff: noqa: E402

# needed to avoid
# RuntimeError: Working outside of application context.
import eventlet
eventlet.monkey_patch()

# expost config object
import os
from pathlib import Path

class Config:
  def __init__(self):
    self._default_apps_folder = Path(os.environ.get("HOSTED_FLASKS_APPS_FOLDER", Path())).resolve()
    self._apps_folder = None

  @property
  def apps_folder(self):
    if self._apps_folder:
      return self._apps_folder
    return self._default_apps_folder
  
  @apps_folder.setter
  def apps_folder(self, value):
    self._apps_folder = Path(value)

config = Config()

# apply some patches to allow existing applications to work as transparantly
# as possible
from hosted_flasks import monkeypatch # noqa
