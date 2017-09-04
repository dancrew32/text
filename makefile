run:
	python app.py

timezone:
	heroku config:add TZ="America/Los_Angeles" -a danmasq-text

logs:
	heroku logs -n 500 -a danmasq-text --tail

deploy:
	git add -A && git commit && git push origin master

settings:
	open https://dashboard.heroku.com/apps/danmasq-text/settings

yelp:
	open https://www.yelp.com/developers/v3/manage_app
