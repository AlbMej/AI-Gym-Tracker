## Setup
Make sure to have Python3, virtualenv, and PostgreSQL already pre-installed.

1. Create a virtual environment by running the command `virtualenv env --python=python3.7`
2. Activate the virtual environment by running `. env/bin/activate`
3. Run the following command `sudo apt-get install libpq-dev`
4. Install the dependencies via `pip3 install -r requirements.txt`


## Set up project on a Heroku server

Make sure to have the Heroku CLI pre installed. In my Ubuntu 18.04 terminal, I used `curl https://cli-assets.heroku.com/install-ubuntu.sh | sh`

1. Login to Heroku: `heroku login`
3. Add python buildpack for Heroku: ` heroku buildpacks:set heroku/python` 
2. Add the Heroku remote to the local repository: `heroku git:remote -a yourapp` 

   In this case, `heroku git:remote -a ai-gym-tracker`
3. Set the settings module: `heroku config:set DJANGO_SETTINGS_MODULE=gym_app.settings.heroku`

## TODO: