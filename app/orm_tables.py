from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb://root:root@localhost:3306/assoc_chat'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(100), nullable=False)
    sexe = db.Column(db.String(100), nullable=False)
    naissance = db.Column(db.String(100), nullable=False)
    race = db.Column(db.String(100), nullable=False)
    robe = db.Column(db.String(100), nullable=False)
    vaccin = db.Column(db.String(100), nullable=False)
    sterilisation = db.Column(db.String(100), nullable=False)
    identification = db.Column(db.String(100), nullable=False)
    deparasitage = db.Column(db.String(100), nullable=False)
    commentaire = db.Column(db.String(3000), nullable=False)
    photo = db.Column(db.String(100), nullable=False)
    carousel = db.Column(db.String(500), nullable=False)


class MessageContact(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    adresse = db.Column(db.String(100), nullable=False)
    code_postal = db.Column(db.String(100), nullable=False)
    ville = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telephone = db.Column(db.String(100), nullable=False)
    objet = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(3000), nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False)  # Aucune idée si ça marche


if __name__ == "__main__":
    # db.create_all()
    # user_test = User(username='test', password='test')
    # db.session.add(user_test)
    # db.session.commit()
    test_select_user = db.session.query(User).filter_by(username='test').filter_by(password="test").first()
    print(test_select_user)

