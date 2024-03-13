import json

from hosted_flasks import scanner
from hosted_flasks import server

print(json.dumps(scanner.find_apps(server.APPS_FOLDER), indent=2, default=str))
