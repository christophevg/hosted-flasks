import logging

import os

from pathlib import Path

from flask import Flask, render_template

logger = logging.getLogger(__name__)

TEMPLATE_FOLDER = os.environ.get(
  "HOSTED_FLASKS_TEMPLATE_FOLDER",
  Path(__file__).resolve().parent / "templates"
)
logger.info(f"using template_folder: {TEMPLATE_FOLDER}")

app = Flask("hosted-flasks", template_folder=TEMPLATE_FOLDER)

apps = {}

@app.route("/")
def show_frontpage():
  return render_template("frontpage.html", apps=apps)
