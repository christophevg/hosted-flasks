import logging

from werkzeug.middleware.dispatcher import DispatcherMiddleware

from hosted_flasks import frontpage
from hosted_flasks.loader import get_apps

# setup logging to stdout

import os

LOG_LEVEL = os.environ.get("LOG_LEVEL") or "INFO"
FORMAT    = "[%(asctime)s] [%(process)d] [%(levelname)s] [%(name)s] %(message)s"
DATEFMT   = "%Y-%m-%d %H:%M:%S %z"

logging.basicConfig(level=LOG_LEVEL, format=FORMAT, datefmt=DATEFMT)
formatter = logging.Formatter(FORMAT, DATEFMT)
logging.getLogger().handlers[0].setFormatter(formatter)

logger = logging.getLogger(__name__)

# dispatch apps based on path and/or hostname

class DomainDispatcher:
  def __init__(self, apps, default=None):
    self.apps    = apps
    self.default = default

  def __call__(self, environ, start_response):
    return self.apps.get(environ["HTTP_HOST"], self.default)(environ, start_response)

# combine the apps with the frontpage

app = DomainDispatcher({ app.hostname : app.handler for app in get_apps() },
  default=DispatcherMiddleware(frontpage.app, {
    app.path : app.handler for app in get_apps()
  })
)

logger.info(f"✅ {len(get_apps())} hosted flasks up & running...")
