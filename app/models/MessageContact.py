from app.app import db


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
    timestamp = db.Column(db.TIMESTAMP, nullable=False)
