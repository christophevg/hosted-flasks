import logging

from pathlib import Path
import importlib.util
import sys

logger = logging.getLogger(__name__)

def find_apps(apps_folder):
  """
  given a folder, finds all Flask apps and returns them as a dict with keys
  path-name and value the flask app
  """
  logger.info(f"loading apps from: {apps_folder}")
  apps = {}
  for folder in Path(apps_folder).iterdir():
    if folder.is_dir():
      logger.info(f"loading {folder.name}")
      try:
        spec = importlib.util.spec_from_file_location(folder.name, folder / "__init__.py")
        mod = importlib.util.module_from_spec(spec)
        sys.modules[folder.name] = mod
        spec.loader.exec_module(mod)
        app = getattr(mod, "app")
        app_name = str(folder.name)
        apps[f"/{app_name}"] = app
      except FileNotFoundError:
        pass
      except AttributeError:
        logger.warning(f"'{folder.name}' doesn't provide 'app'")
  return apps
