__version__ = "0.0.5"

# ruff: noqa: E402

# needed to avoid
# RuntimeError: Working outside of application context.
import eventlet
eventlet.monkey_patch()

# apply some patches to allow existing applications to work as transparantly
# as possible
from hosted_flasks import monkeypatch # noqa
