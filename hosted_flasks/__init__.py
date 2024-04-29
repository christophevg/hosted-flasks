__version__ = "0.0.8"

# ruff: noqa: E402

# needed to avoid
# RuntimeError: Working outside of application context.
import eventlet
eventlet.monkey_patch()

# load the environment variables for this setup from .env file
from dotenv import load_dotenv
load_dotenv()
load_dotenv(".env.local")

# apply some patches to allow existing applications to work as transparantly
# as possible
from hosted_flasks import monkeypatch # noqa
