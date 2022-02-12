from app.app import db


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
