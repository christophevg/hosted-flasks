RUN_CMD=HOSTED_FLASKS_APPS_FOLDER=apps gunicorn hosted_flasks.server:app

cli: env-run
	@HOSTED_FLASKS_APPS_FOLDER=apps python -m hosted_flasks
