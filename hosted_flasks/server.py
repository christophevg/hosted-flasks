import logging

from werkzeug.middleware.dispatcher import DispatcherMiddleware

from hosted_flasks import scanner
from hosted_flasks import frontpage

logger = logging.getLogger(__name__)

# load modules/apps dynamically

apps = scanner.find_apps()
frontpage.apps = apps

class DomainDispatcher:
  def __init__(self, apps, default=None):
    self.apps    = apps
    self.default = default

  def __call__(self, environ, start_response):
    return self.apps.get(environ["HTTP_HOST"], self.default)(environ, start_response)

# combine the apps with the frontpage

app = DomainDispatcher({ app.hostname : app.handler for app in apps },
  default=DispatcherMiddleware(frontpage.app, {
    app.path : app.handler for app in apps
  })
)

logger.info(f"✅ {len(apps)} hosted flasks up & running...")
