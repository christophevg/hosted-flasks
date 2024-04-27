import logging

import os

from pathlib import Path
import importlib.util
import sys
from dotenv import dotenv_values

from dataclasses import dataclass, field

from flask import Flask

logger = logging.getLogger(__name__)

APPS_FOLDER = Path(os.environ.get("HOSTED_FLASKS_APPS_FOLDER", Path())).resolve()

@dataclass
class HostedFlask:
  name    : str
  handler : Flask = field(repr=False)
  hostname: str = None
  path    : str = None

def find_apps(apps_folder=APPS_FOLDER):
  """
  detects Flask apps in the given location
  """
  logger.info(f"👀 looking for apps in {apps_folder}")
  apps = []
  for folder in Path(apps_folder).iterdir():
    if folder.is_dir():
      try:
        spec = importlib.util.spec_from_file_location(folder.name, folder / "__init__.py")
        mod = importlib.util.module_from_spec(spec)
        sys.modules[folder.name] = mod
        spec.loader.exec_module(mod)
        
        name = folder.name
        handler = getattr(mod, "app")

        env = dotenv_values(folder / ".env")
        hostname = env.get("HOSTED_FLASKS_HOSTNAME", None)
        path = env.get("HOSTED_FLASKS_PATH", None)

        if hostname or path:
          app = HostedFlask(name, handler, hostname, path)
          apps.append(app)
          logger.info(f"🌎 imported {app.name}")
        else:
          logger.warning(f"⛔️ '{folder.name}' provides 'app' without hostname or path")
      except FileNotFoundError:
        pass
      except AttributeError:
        logger.warning(f"😞 '{folder.name}' doesn't provide 'app'")
  return apps
