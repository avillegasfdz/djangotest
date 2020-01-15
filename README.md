# djangotest
Django app for the test application.

## Project structure:

* core: Django application
* poc: Directory reserved for proof-of-concept purposes
* unittest: Unit tests of the application

## Project Setup:
These set up instuctions are for Ubuntu 18.04

Install Docker following the [official instructions](https://docs.docker.com/install/linux/docker-ce/ubuntu/).
Do not forget to excecute the [post-installation steps](https://docs.docker.com/install/linux/linux-postinstall/).
Install docker-compose (`sudo apt-get install docker-compose`)

Get the docker image for Postgres (`docker pull postgres`)

Please install the following packages (assuming `python` points to your Python 3 installation):
* Django: `python -m pip install Django`
* Required package for PostgreSQL `python -m pip install psycopg2` 
(Note: this Python package has a dependency with PostgreSQL devel in Ubuntu.
If the installation fails, please install `sudo apt-get install libpq-dev`)
* Django all auth: `python -m pip install django-allauth`
* LocalFlavor: `python -m pip install localflavor`


## Initialization
* Start the Postgres Docker container: `docker-compose -f stack.yml up`
* Create the superuser: `python manage.py createsuperuser`
* Add Google as social application with name=GL, 
client_id=981887593937-be448n97e939ictakl7kaikmqqlrfu6g.apps.googleusercontent.com
and secret=J0y4bq5e6mS-MNqFeWvjMnBS

