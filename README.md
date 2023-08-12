# STUDENTLINK BACKEND

StudentLink is a tool for matching student's with potential roommates and landlords.

## INSTALL

Studentlink uses a Python virtual environment.

To setup the virtual environment, change directory to the repo.

Create a virtual environment
`python -m venv venv`

activate the virtual environment
`source venv/bin/activate`

install the dependencies in requirements.txt
`pip install -r requirements.txt`


## DEVELOP

activate the virtual environment if you have not already.
`source venv/bin/activate`

create an .env file
`cp env.sample .env`

start the application
`python flaskapp.py`


## RELEASE

Submit a pull request from `main` to `release` to ship code to production.


