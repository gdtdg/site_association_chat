from app.orm_tables import db


def db_insert(variable):
    db.session.add(variable)
    db.session.commit()


def db_delete(variable):
    db.session.db_delete(variable)
    db.session.commit()
