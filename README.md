# djangotest
Django app for the test application.

## Project structure:

* core: Django application
* poc: Directory reserved for proof-of-concept purposes
* unittest: Unit tests of the application

## Project Setup:

Please install the following packages (assuming `python` points to your Python 3 installation):
* Django: `python -m pip install Django`
* Required package for PostgreSQL `python -m pip install psycopg2` 
(Note: this Python package has a dependency with PostgreSQL devel in Ubuntu.
If the installation fails, please install `sudo apt-get install libpq-dev`)
* Django all auth: `python -m pip install django-allauth`

