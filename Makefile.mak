RUN_CMD=HOSTED_FLASKS_APPS_FOLDER=apps gunicorn -k eventlet -w 1 hosted_flasks.server:app

cli: env-run
	@HOSTED_FLASKS_APPS_FOLDER=apps python -m hosted_flasks
