# Getting Started

Typical usage:

```console
% mkdir my_apps
% cd my_apps
```

Now create one or more flask apps, each in their own module/folder:

```console
% tree .                     
.
├── backend
│   └── __init__.py
├── frontend
│   └── __init__.py
└── templates
    └── frontpage.html
```

For example containing the minimal Hello World Flask application:

```console
% cat backend/__init__.py 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello My Backend"
```

Optionally, but highly recommended: set up a virtual environment.

```console
% pyenv virtualenv my_apps
% pyenv local my_apps
```

Install `hosted-flasks` and `gunicorn` (or your other favorite WSGI server)

```console
% pip install hosted_flasks gunicorn

% HOSTED_FLASKS_APPS_FOLDER=. gunicorn hosted_flask.server:app
[2024-03-13 10:08:55 +0100] [80171] [INFO] Starting gunicorn 21.2.0
[2024-03-13 10:08:55 +0100] [80171] [INFO] Listening at: http://127.0.0.1:8000 (80171)
[2024-03-13 10:08:55 +0100] [80171] [INFO] Using worker: sync
[2024-03-13 10:08:55 +0100] [80198] [INFO] Booting worker with pid: 80198
[hosted_flasks] [INFO] loading frontend
[hosted_flasks] [INFO] loading backend
```
