import logging
import os

from werkzeug.middleware.dispatcher import DispatcherMiddleware

import hosted_flasks.log_setup #noqa

from hosted_flasks import scanner
from hosted_flasks import frontpage

logger = logging.getLogger(__name__)

# load modules/apps dynamically

APPS_FOLDER = os.environ.get("HOSTED_FLASKS_APPS_FOLDER", "apps")
apps = scanner.find_apps(APPS_FOLDER)
frontpage.apps = apps

# combine the apps with the frontpage

app = DispatcherMiddleware(frontpage.app, apps)
