from hosted_flasks.loader import get_apps

def test_ensure_exception_when_default_config_file_is_not_found():
  try:
    get_apps(force=True)
    assert False, "expected ValueError due to missing config file"
  except ValueError:
    pass

def test_app_loading(tmp_path):
  app_names = [ "app_1", "app_2" ]

  # create 2 miminal apps
  for app_name in app_names:
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

  # create a configuration
  config = tmp_path / "hosted-flasks.yaml"
  content = ""
  for app_name in app_names:
    content += f"""
{app_name}:
  src: {app_name}
  path: /{app_name}
  hostname: {app_name}
"""
  config.write_text(content)

  apps = get_apps(config, force=True)
  assert len(apps) == 2
  assert [ app.name for app in apps ] == [ "app_1", "app_2" ]

  # apps need at least a path or a hostname
  content += f"""
not_served:
  src: {app_name}
"""
  config.write_text(content)

  apps = get_apps(config, force=True)
  assert len(apps) == 2
  assert [ app.name for app in apps ] == [ "app_1", "app_2" ]

  # add dummy app without actual implementation/src of FileNotFound
  content += """
dummy:
  src: dummy
  path: /dummy
"""
  config.write_text(content)

  apps = get_apps(config, force=True)
  assert len(apps) == 2
  assert [ app.name for app in apps ] == [ "app_1", "app_2" ]

  # add dummy implementation, without exposing a Flask object
  dummy = tmp_path / "dummy"
  dummy.mkdir()
  init = dummy / "__init__.py"
  init.write_text("# nothing here")
  
  apps = get_apps(config, force=True)
  assert len(apps) == 2
  assert [ app.name for app in apps ] == [ "app_1", "app_2" ]
