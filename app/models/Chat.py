from app.app import db


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(100), nullable=False)
    sexe = db.Column(db.String(100), nullable=False)
    naissance = db.Column(db.String(100), nullable=True)
    race = db.Column(db.String(100), nullable=True)
    robe = db.Column(db.String(100), nullable=True)
    vaccin = db.Column(db.String(100), nullable=True)
    sterilisation = db.Column(db.String(100), nullable=True)
    identification = db.Column(db.String(100), nullable=True)
    deparasitage = db.Column(db.String(100), nullable=True)
    commentaire = db.Column(db.String(3000), nullable=True)
    photo = db.Column(db.String(100), nullable=True)
    carousel = db.Column(db.String(500), nullable=True)
