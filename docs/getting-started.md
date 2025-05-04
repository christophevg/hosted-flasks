# Getting Started

Typical usage:

```console
% mkdir my_apps
% cd my_apps
```

First create one or more flask apps, each in their own module/folder:

```console
% tree .
.
├── backend
│   └── __init__.py
├── frontend
│   └── __init__.py
└── hosted-flasks.yaml
```

Each containing for example a minimal Hello World Flask application:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello My Backend"
```

Next, we create a YAML configuration file, `hosted-flasks.yaml`, containing the flask apps we want to be served and how we want them to be served:

```yaml
backend:
  imports:
    backend: backend/__init__.py
  path: /backend
  hostname: backend.localhost:8000

frontend:
  imports:
    frontend: frontend/__init__.py
  path: /frontend
  hostname: frontend.localhost:8000
```

In this case we want both apps served from a path on the default application (`/backend` and `/frontend`), as well as on a custom hostname (`backend.localhost:8000` and `frontend.localhost:8000`).

Optionally, but highly recommended 😇, set up a virtual environment:

```console
% pyenv virtualenv my_apps
% pyenv local my_apps
```

Install `hosted-flasks` and `gunicorn` (or your other favorite WSGI server) and start the Hosted Flasks server app:

```console
% pip install hosted-flasks gunicorn eventlet

% gunicorn -k eventlet -w 1 hosted_flasks.server:app
[2024-04-28 15:35:46 +0200] [5320] [INFO] Starting gunicorn 22.0.0
[2024-04-28 15:35:46 +0200] [5320] [INFO] Listening at: http://127.0.0.1:8000 (5320)
[2024-04-28 15:35:46 +0200] [5320] [INFO] Using worker: eventlet
[2024-04-28 15:35:46 +0200] [5347] [INFO] Booting worker with pid: 5347
[2024-04-28 15:35:46 +0200] [5347] [INFO] [hosted_flasks.loader] 🌍 added backend
[2024-04-28 15:35:46 +0200] [5347] [INFO] [hosted_flasks.loader] 🌍 added frontend
[2024-04-28 15:35:46 +0200] [5347] [INFO] [hosted_flasks.server] ✅ 2 hosted flasks up & running...
```

You can now visit your backend Flask app from e.g.

* [http://localhost:8000/backend](http://localhost:8000/backend)
* [http://backend.localhost:8000](http://backend.localhost:8000)

And when visiting the root [http://localhost:8000](http://localhost:8000) you are presented with a frontpage listing the Hosted Flasks with links to their hosted locations:

![Hosted Flasks Frontpage](_static/frontpage.png)
