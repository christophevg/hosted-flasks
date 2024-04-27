import os

from hosted_flasks import config
from hosted_flasks.scanner import find_apps

def test_app_specific_environment_variable(tmp_path):
  config.apps_folder = tmp_path

  # setup app with .env
  for app_name in [ "app_1" ]:
    folder = tmp_path / app_name
    folder.mkdir()
    init = folder / "__init__.py"
    init.write_text("""
from flask import Flask
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

app = Flask(__name__)

NAME = os.environ.get("NAME")

@app.route("/")
def hello_world():
  return f"Hello {NAME}"  
""")
    env = folder / ".env"
    env.write_text(f"""
HOSTED_FLASKS_PATH=/{app_name}
{app_name.upper()}_NAME=AppSpecific
""")
  apps = find_apps()
  assert len(apps) == 1

  html = apps[0].handler.test_client().get("/")
  assert os.environ.get("APP_1_NAME") == "AppSpecific" # loaded by dotenv
  assert html.data == b"Hello AppSpecific"
