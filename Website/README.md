## Setup
Make sure to have Python3, virtualenv, and PostgreSQL already pre-installed.

1. Create a virtual environment by running the command `virtualenv env --python=python3.7`
2. Activate the virtual environment by running `. env/bin/activate` or `source env/bin/activate`
3. Install the dependencies via `pip install -r requirements.txt`

## Set up project on a Heroku server (I have already done this part for you)

Make sure to have the Heroku CLI pre installed. In my Ubuntu 18.04 terminal, I used `curl https://cli-assets.heroku.com/install-ubuntu.sh | sh`

1. Login to Heroku: `heroku login`
2. Add the Heroku remote to the local repository: `heroku git:remote -a rcos-gym-tracker` 
3. Add python buildpack for Heroku: ` heroku buildpacks:set heroku/python` 
4. Set dynos: `heroku ps:scale web=1 --app rcos-gym-tracker`
5. Set the settings module: `heroku config:set DJANGO_SETTINGS_MODULE=gym_app.settings.heroku`
6. Migrate the database: `heroku run python Website/manage.py migrate`

## Run project locally

1. Run: `python manage.py runserver`

## TODO:
Write better readme
