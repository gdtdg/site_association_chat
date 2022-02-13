from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb://root:root@localhost:3306/assoc_chat'
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
