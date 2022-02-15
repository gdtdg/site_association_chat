# Association des chat de la street website

A fictional cat protection website.

## Installation

### Requirements

Python 3.9 required.

Python packages required : ```pip install -r requirements.txt```

## Instructions

You need to change in `config_template.toml`: the`secret key`, the `connection string to database`
and the `upload folder` to receive cats images.

Then replace `config_template.toml` name by `config.toml`.

#### How to run the flask server:

Setup the flask environment: `export FLASK_APP='app/routes'`

then start the flask server: `flask run`