import logging
import os

from werkzeug.middleware.dispatcher import DispatcherMiddleware

from hosted_flasks import scanner
from hosted_flasks import frontpage

logger = logging.getLogger(__name__)

# load modules/apps dynamically

APPS_FOLDER = os.environ.get("HOSTED_FLASKS_APPS_FOLDER", "apps")
apps = scanner.find_apps(APPS_FOLDER)
frontpage.apps = apps

class DomainDispatcher:
  def __init__(self, apps, default=None):
    self.apps    = apps
    self.default = default

  def __call__(self, environ, start_response):
    host = environ['HTTP_HOST'].split(":")[0]
    return self.apps.get(host, self.default)(environ, start_response)

# combine the apps with the frontpage

app = DomainDispatcher({ app.hostname : app.handler for app in apps },
  default=DispatcherMiddleware(frontpage.app, {
    app.path : app.handler for app in apps
  })
)
