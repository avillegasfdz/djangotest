# djangotest
Django app for the test application.

## Project structure:

* core: Django application
* poc: Directory reserved for proof-of-concept purposes
* test: Test environment for the application

## Project Setup:
These set up instructions are for Ubuntu 18.04. 
Follow these instructions to create a development and execution environment.
For a testing environment, please go to the section "Test environment setup" of this document.

* Install Docker following the [official instructions](https://docs.docker.com/install/linux/docker-ce/ubuntu/).
Do not forget to excecute the [post-installation steps](https://docs.docker.com/install/linux/linux-postinstall/).
* Install docker-compose (`sudo apt-get install docker-compose`)
* Get the docker image for Postgres (`docker pull postgres`)
Please install the following packages (assuming `python` points to your Python 3 installation):
* Django: `python -m pip install Django`
* Required package for PostgreSQL `python -m pip install psycopg2` 
(Note: this Python package has a dependency with PostgreSQL devel in Ubuntu.
If the installation fails, please install `sudo apt-get install libpq-dev`)
* Django all auth: `python -m pip install django-localflavor`

## Database and Social Account Initialization
The Postgres database is set inside a docker container. Furthermore, the
* Start the Postgres Docker container: `docker-compose -f stack.yml up`
* Create the superuser: `python manage.py createsuperuser`
* Start the server: `python manage.py runserver`
* In your web browser, enter Django as administrator: `localhost:8000/admin`
* Add Google as social application with name=GL, 
client_id=981887593937-be448n97e939ictakl7kaikmqqlrfu6g.apps.googleusercontent.com
and secret=J0y4bq5e6mS-MNqFeWvjMnBS

## Test environment setup
To run the test environment, it is a requirement to set up the database and the Social Account as described in the previous step. Then, follow these instructions.
* Install VirtualBox: `sudo apt install virtualbox` 
* Download Vagrant: `curl -O https://releases.hashicorp.com/vagrant/2.2.6/vagrant_2.2.6_x86_64.deb`
* Install Vagrant: `sudo apt install ./vagrant_2.2.6_x86_64.deb`
* CD to the directory to store the Vagrant image.
* Download the image: `vagrant box add bento/ubuntu-18.04`
* Start the Vagrant file: `vagrant init bento/ubuntu-18.04`
* Configure the Vagrantfile as provided in the `Vagrantfile.org` file.
* Go to the Vagrant directory in `test/vagrant`
* Start Vagrant: `vagrant up`
* Enter Vagrant: `vagrant ssh`
* Configure the VM as described in the "Project Setup" section of this file.
* Enter the directory linked with the source code of the project: `cd code/core/bankmanagement/`
* Run the server `python3 manage.py runserver 0.0.0.0:8000`

The application can be now accessed from http://localhost:8081 in your web browser. 
Make sure that you are not already running an instance of the application in your host machine (i.e., outside Vagrant). 
Otherwise, you will find a conflict in the port configuration.
