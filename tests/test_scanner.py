from hosted_flasks import config
from hosted_flasks.scanner import find_apps

def test_app_detection(tmp_path):
  config.apps_folder = tmp_path
  
  assert find_apps() == []

  # create 2 miminal apps
  for app_name in [ "app_1", "app_2" ]:
    folder = tmp_path / app_name
    folder.mkdir()
    init = folder / "__init__.py"
    init.write_text("""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello World"  
""")
    env = folder / ".env"
    env.write_text("HOSTED_FLASKS_PATH=/hello")

  apps = find_apps()
  assert len(apps) == 2
  assert [ app.name for app in apps ] == [ "app_1", "app_2" ]

  # add 1 valid Flask app that isn't configured to be served
  folder = tmp_path / "unserved"
  folder.mkdir()
  init = folder / "__init__.py"
  init.write_text("""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello World"  
""")

  apps = find_apps()
  assert len(apps) == 2
  assert [ app.name for app in apps ] == [ "app_1", "app_2" ]

  # add dummy folder / coverage of FileNotFound
  dummy = tmp_path / "dummy"
  dummy.mkdir()

  apps = find_apps()
  assert len(apps) == 2
  assert [ app.name for app in apps ] == [ "app_1", "app_2" ]
  
  # add empty __init__.py / coverage of AttributeError
  init = dummy / "__init__.py"
  init.write_text("# nothing here")

  apps = find_apps()
  assert len(apps) == 2
  assert [ app.name for app in apps ] == [ "app_1", "app_2" ]
