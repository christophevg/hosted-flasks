import logging

import os
import sys

from pathlib import Path

import yaml

import importlib.util

from dataclasses import dataclass, field
from typing import Union
from flask import Flask

logger = logging.getLogger(__name__)

apps = []

@dataclass
class HostedFlask:
  name    : str
  src     : Union[str, Path]
  path    : str   = None
  hostname: str   = None
  handler : Flask = field(repr=False, default=None)

  def __post_init__(self):
    if not self.path and not self.hostname:
      logger.fatal(f"⛔️ an app needs at least a path or a hostname: {self.name}")
      return

    self.src = Path(self.src).resolve() # ensure it's a Path

    # we need to add app to apps before loading the handler, because else the
    # monkeypatched os.environ.get won't be able to correct handle calls to it
    # at the time of loading the handler
    apps.append(self)

    # if the handler isn't provided, load it from the source
    if not self.handler:
      self.load_handler()
      
    # without a handler, we remove ourself from the apps
    if not self.handler:
      logger.fatal(f"⛔️ an app needs a handler: {self.name}")
      apps.remove(self)
  
  def load_handler(self):
    # load the module, creating the handler flask app
    try:
      spec = importlib.util.spec_from_file_location(self.src.name, self.src / "__init__.py")
      mod = importlib.util.module_from_spec(spec)
      sys.modules[self.src.name] = mod
      spec.loader.exec_module(mod)
    
      # TODO flask object location from settings
      self.handler = getattr(mod, "app")
    except FileNotFoundError:
      logger.warning(f"😞 '{self.src.name}' doesn't provide '__init__.py'")
    except AttributeError:
      logger.warning(f"😞 '{self.src.name}' doesn't provide 'app'")

def add_app(name, src, path=None, hostname=None, handler=None):
  app = HostedFlask(name, src, path, hostname, handler)
  logger.info(f"🌍 added {app.name}")

def get_apps(config=None, force=False):
  global apps

  if force:
    apps.clear()

  # lazy load the apps
  if not apps:
    if not config:
      config = os.environ.get("HOSTED_FLASKS_CONFIG", Path() / "hosted-flasks.yaml")
    try:
      with open(config) as fp:
        for name, settings in yaml.safe_load(fp).items():
          src = config.parent / settings.pop("src")
          add_app(name, src, **settings)
    except FileNotFoundError:
      raise ValueError(f"💀 I need a config file. Tried: {config}")
  return apps
