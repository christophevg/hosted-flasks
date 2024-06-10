# TODO

## version 0.1.0

- [x] load and serve apps from a subfolder path
- [x] frontpage with links to apps in subfolders paths
- [x] load and serve apps from a hostname
- [x] frontpage with links to apps on hostname
- [x] move hosted flasks configuration from .env to root-level config file
  - [x] consider: changing scanner into loader based on root-level config file
- [x] enable more complex app structures, e.g. module.submodule.app
- [x] provide tools for apps
  - [x] for working with "local" environments
  - [x] import app specific .env with prefix by default
- [x] load own .env(.local)
- [x] add more information
  - [x] link to GitHub repo
  - [x] last updated timestamp
  - [x] image
  - [x] README/description (markdown)
- [ ] status page
- [ ] improve code/testability more

## later 😇

- [ ] use app marked as default in stead of default frontpage
- [ ] tooling for working with subfolder paths vs absolute paths on hostname
- [ ] consider: monkeypatching logging.getLogger().handlers[0].setFormatter
