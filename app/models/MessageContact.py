from sqlalchemy import func

from app.app import db


class MessageContact(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=True)
    adresse = db.Column(db.String(100), nullable=True)
    code_postal = db.Column(db.String(100), nullable=True)
    ville = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=False)
    telephone = db.Column(db.String(100), nullable=True)
    objet = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(3000), nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=True, default=func.now())
