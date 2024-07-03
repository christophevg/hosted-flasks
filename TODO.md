# TODO

## Now

- [x] update documentation, make it up to date with 0.1.0 version
  - [ ] extend documentation with all features, beyond getting started

## version 0.1.x

- [ ] add support for health url
  - [ ] status page/indicators (depends on health url)
- [ ] improve code/testability more
- [ ] add tags with categories

## unprioritized backlog 😇

- [ ] use app marked as default in stead of default frontpage
- [ ] tooling for working with subfolder paths vs absolute paths on hostname
- [ ] consider: monkey patching logging.getLogger().handlers[0].setFormatter
- [ ] all info as json (?)
  - [ ] default frontpage -> dynamic
- [ ] usage statistics?
- [ ] centralized logging? where to, to avoid too much overhead with every call

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
- [x] apply bootstrap
- [x] add more information
  - [x] link to GitHub repo
  - [x] last updated timestamp
  - [x] image
  - [x] README/description (markdown)
