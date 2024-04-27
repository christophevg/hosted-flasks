import logging
import os

from hosted_flasks import scanner

# setup logging to stdout

logger = logging.getLogger(__name__)

LOG_LEVEL = os.environ.get("LOG_LEVEL") or "WARNING"
FORMAT    = "[%(name)s] [%(levelname)s] %(message)s"
DATEFMT   = "%Y-%m-%d %H:%M:%S %z"

logging.basicConfig(level=LOG_LEVEL, format=FORMAT, datefmt=DATEFMT)
formatter = logging.Formatter(FORMAT, DATEFMT)
logging.getLogger().handlers[0].setFormatter(formatter)

def cli():
  for app in scanner.find_apps():
    print(f"{app.name} is hosted on")
    if app.path:
      print(f" - from path {app.path}")
    if app.hostname:
      print(f" - from hostname {app.hostname}")

if __name__ == "__main__":
  cli()
