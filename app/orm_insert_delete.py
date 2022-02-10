from app.orm_tables import db


def insert(variable):
    db.session.add(variable)
    db.session.commit()


def delete(variable):
    db.session.delete(variable)
    db.session.commit()
