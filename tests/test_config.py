from hosted_flasks.scanner import find_apps

def test_dotenv_loading(tmp_path):
  # setup app with .env
  for app_name in [ "app_1" ]:
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
    env.write_text(f"""
HOSTED_FLASKS_HOSTNAME={app_name}
HOSTED_FLASKS_PATH=/{app_name}
""")
  apps = find_apps(tmp_path)
  assert len(apps) == 1
  assert apps[0].name     == app_name
  assert apps[0].hostname == app_name
  assert apps[0].path     == f"/{app_name}"
