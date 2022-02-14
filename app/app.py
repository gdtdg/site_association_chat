import toml as toml
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_file("config.toml", load=toml.load)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


def db_insert(variable):
    db.session.add(variable)
    db.session.commit()


def db_delete(variable):
    db.session.delete(variable)
    db.session.commit()
