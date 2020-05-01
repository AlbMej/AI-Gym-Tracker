# GymApp Webapp Setup 

A Modern web application with Django and ReactJS. 
Make sure to have Python3, virtualenv, and PostgreSQL already pre-installed.
Make sure to clone the repo before continuing with the following steps.

# Install Python 3.8 (Ubuntu 18.04)

1. Update the packages list and install the prerequisites:
	```
	sudo apt update
	sudo apt install software-properties-common
	```
2. Add the deadsnakes PPA to your system’s sources list using the following command: `sudo add-apt-repository ppa:deadsnakes/ppa`
3. Install Python 3.8 using the following command: `sudo apt install python3.8`
4. You can check if Python 3.8 is installed using the following command: `python3.8 --version`

# Create Virtual Environment

1. Check to see which pip points to Python 3 by using: `pip --version` and `pip3 --version`
2. Use the pip associated with Python 3 and install virtualenv: `pip install virtualenv` or `pip3 install virtualenv`
   Here is a template on how to create a python virtual env: `virtualenv DIR_NAME --python=python3.x`
3. Create virtual env:  `virtualenv env --python=python3.8`
4. Activate the virtual environment by running `. env/bin/activate` or `source env/bin/activate`
5. Type `deactivate` to exit the virtual environment. 

# Install Dependencies

1. Upgrade pip: `pip install --upgrade pip` or `pip install --upgrade --user pip`
2. Install the dependencies via `pip install -r requirements.txt`


# How to run the project

- Activate the virtual environment
- `$ cd GymApp/frontend`
- `$ npm install`
- `$ npm run start`
- `$ python manage.py runserver`