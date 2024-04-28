import logging
import os

from flask import Flask

# setup logging to stdout
LOG_LEVEL = os.environ.get("LOG_LEVEL") or "INFO"
FORMAT    = "[%(asctime)s] [%(process)d] [%(levelname)s] [%(name)s] %(message)s"
DATEFMT   = "%Y-%m-%d %H:%M:%S %z"

logging.basicConfig(level=LOG_LEVEL, format=FORMAT, datefmt=DATEFMT)
formatter = logging.Formatter(FORMAT, DATEFMT)
logging.getLogger().handlers[0].setFormatter(formatter)

logger = logging.getLogger(__name__)

# create app
custom_app = Flask(__name__)

@custom_app.route("/")
def hello_world():
  return "Hello Complex"
