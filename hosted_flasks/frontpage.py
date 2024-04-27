import logging

import os

from pathlib import Path

from flask import Flask, render_template

logger = logging.getLogger(__name__)

TEMPLATE_FOLDER = os.environ.get("HOSTED_FLASKS_TEMPLATE_FOLDER", None)
if not TEMPLATE_FOLDER:
  TEMPLATE_FOLDER = Path(__file__).resolve().parent / "templates"
  logger.debug("📰 using default template folder")
else:
  TEMPLATE_FOLDER = Path(TEMPLATE_FOLDER).resolve()
  logger.debug(f"📰 using template folder: {TEMPLATE_FOLDER.relative_to(Path.cwd())}")

app = Flask("hosted-flasks", template_folder=TEMPLATE_FOLDER)

apps = [] # to be filled externally with apps that are served, see server.py

@app.route("/")
def show_frontpage():
  return render_template("frontpage.html", apps=apps)
