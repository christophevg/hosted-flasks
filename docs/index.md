# Hosted Flasks

> serve flask apps side by side

[![Latest Version on PyPI](https://img.shields.io/pypi/v/hosted-flasks.svg)](https://pypi.python.org/pypi/hosted-flasks/)
[![Supported Implementations](https://img.shields.io/pypi/pyversions/hosted-flasks.svg)](https://pypi.python.org/pypi/hosted-flasks/)
![Build Status](https://github.com/christophevg/hosted-flasks/actions/workflows/test.yaml/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/hosted-flasks/badge/?version=latest)](https://hosted-flasks.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/christophevg/hosted-flasks/badge.svg?branch=master)](https://coveralls.io/github/christophevg/hosted-flasks?branch=master)
[![Built with PyPi Template](https://img.shields.io/badge/PyPi_Template-v0.5.0-blue.svg)](https://github.com/christophevg/pypi-template)

Hosted Flasks implements the concept of [Flask's Application Dispatching](https://flask.palletsprojects.com/en/3.0.x/patterns/appdispatch/), wrapping it in a module with some operational supporting tools.

It essentially allows for dynamically detecting and loading separate Flask apps from a given folder and serves them side by side as apparently separate Flask apps, under a separate folder or different hostname, yet form a single instance. So, basically, you only need a single "server" to host multiple applications, which is my personal reason for its existence and development. 

> I have several small Flask apps, which don't use a lot of resources. For some time I'm enjoying the hosting services of [Render](https://render.com). Their free tier is great, but (understandably) "_free instances will spin down with inactivity, which can delay requests by 50 seconds or more._". Their [web service pricing](https://render.com/pricing#compute) is more than reasonable, yet coughing up $7/month for each single little Flask app is a bit too much. So, with Hosted Flasks I can simply bring them all together on a single web service, which doesn't spin down.

Hosted Flasks adds serveral utilities on top of Flask's Application Dispatching, to make the virtual hosting as transparant as possible. It can also serves a top-level frontpage-like app, e.g. listing the apps by default. 

## Contents

```{toctree}
:maxdepth: 1
getting-started.md
contributing.md
```

