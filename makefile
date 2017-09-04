run:
	python app.py

timezone:
	heroku config:add TZ="America/Los_Angeles" -a danmasq-text

logs:
	heroku logs -n 500 -a danmasq-text --tail
