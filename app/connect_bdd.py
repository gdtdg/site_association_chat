# Tout le contenu de ce fichier ne sert plus, il a été remplacé par l'ORM.

import mysql.connector


def insert_stuff(var):
    connection = mysql.connector.connect(host='localhost', user='root', passwd='root', database='assoc_chat')
    cursor = connection.cursor()
    new_chat = {
        "nom": var,
    }
    cursor.execute("INSERT INTO chat (nom) VALUES (%(nom)s)", new_chat)
    connection.commit()
    cursor.close()
    connection.close()


def select_all_cats():
    connection = mysql.connector.connect(host='localhost', user='root', passwd='root', database='assoc_chat')
    cursor = connection.cursor()
    query = "SELECT nom, sexe, naissance, race, robe, vaccin, sterilisation, identification, deparasitage, commentaire, photo, id FROM chat"

    cursor.execute(query)
    my_cats = []
    for (nom, sexe, naissance, race, robe, vaccin, sterilisation, identification, deparasitage, commentaire, photo,
         id) in cursor:
        my_cat = {'nom': nom, 'sexe': sexe, 'naissance': naissance, 'race': race, 'robe': robe, 'vaccin': vaccin,
                  'sterilisation': sterilisation, 'identification': identification, 'deparasitage': deparasitage,
                  'commentaire': commentaire, 'photo': photo, 'id': id}
        my_cats.append(my_cat)
    ret = {"data": my_cats}
    cursor.close()
    connection.close()
    return ret


def select_all_messages():
    connection = mysql.connector.connect(host='localhost', user='root', passwd='root', database='assoc_chat')
    cursor = connection.cursor()
    query = "SELECT id, nom, prenom, adresse, code_postal, ville, \
         email, telephone, objet, message, timestamp FROM message_contact"

    cursor.execute(query)
    my_messages = []
    for (id, nom, prenom, adresse, code_postal, ville,
         email, telephone, objet, message, timestamp) in cursor:
        my_message = {'id': id, 'nom': nom, 'prenom': prenom, 'adresse': adresse, 'code_postal': code_postal,
                      'ville': ville, 'email': email, 'telephone': telephone, 'objet': objet, 'message': message,
                      'timestamp': timestamp}
        my_messages.append(my_message)
    ret = {"data": my_messages}
    cursor.close()
    connection.close()
    return ret


def delete_message(id_message):
    connection = mysql.connector.connect(host='localhost', user='root', passwd='root', database='assoc_chat')
    cursor = connection.cursor()
    query = "DELETE FROM message_contact WHERE id=%s"
    cursor.execute(query, [id_message])
    connection.commit()
    cursor.close()
    connection.close()


def select_one_cat(id_chat):
    connection = mysql.connector.connect(host='localhost', user='root', passwd='root', database='assoc_chat')
    cursor = connection.cursor()

    query = "SELECT nom, sexe, naissance, race, robe, vaccin, sterilisation, identification, deparasitage, commentaire, photo, carousel FROM chat WHERE id=%s"

    cursor.execute(query, [id_chat])
    my_cat = {}
    for (nom, sexe, naissance, race, robe, vaccin, sterilisation, identification, deparasitage, commentaire,
         photo, carousel) in cursor:
        my_cat['nom'] = nom
        my_cat['sexe'] = sexe
        my_cat['naissance'] = naissance
        my_cat['race'] = race
        my_cat['robe'] = robe
        my_cat['vaccin'] = vaccin
        my_cat['sterilisation'] = sterilisation
        my_cat['identification'] = identification
        my_cat['deparasitage'] = deparasitage
        my_cat['commentaire'] = commentaire
        my_cat['photo'] = photo
        my_cat['carousel'] = carousel
    cursor.close()
    connection.close()
    return my_cat


def insert_message(nom, prenom, adresse, code_postal, ville, email, telephone, objet, message):
    connection = mysql.connector.connect(host='localhost', user='root', passwd='root', database='assoc_chat')
    cursor = connection.cursor()
    new_message = {
        "nom": nom,
        "prenom": prenom,
        "adresse": adresse,
        "code_postal": code_postal,
        "ville": ville,
        "email": email,
        "telephone": telephone,
        "objet": objet,
        "message": message
    }
    cursor.execute(
        "INSERT INTO message_contact (nom, prenom, adresse, code_postal, ville,\
         email, telephone, objet, message) VALUES (%(nom)s, %(prenom)s,%(adresse)s,\
         %(code_postal)s,%(ville)s,%(email)s,%(telephone)s,%(objet)s,%(message)s)",
        new_message)
    connection.commit()
    cursor.close()
    connection.close()


def select_user(username, password):
    connection = mysql.connector.connect(host='localhost', user='root', passwd='root', database='assoc_chat')
    cursor = connection.cursor()

    query = "SELECT username, password FROM user WHERE username=%s AND password=%s"

    cursor.execute(query, [username, password])
    user = {}
    for (username, password) in cursor:
        user['username'] = username
        user['password'] = password

    cursor.close()
    connection.close()
    return user


def insert_chat(nom, sexe, naissance, race, robe, vaccin, sterilisation, identification, deparasitage, commentaire,
                photo, carousel):
    connection = mysql.connector.connect(host='localhost', user='root', passwd='root', database='assoc_chat')
    cursor = connection.cursor()
    new_chat = {
        "nom": nom,
        "sexe": sexe,
        "naissance": naissance,
        "race": race,
        "robe": robe,
        "vaccin": vaccin,
        "sterilisation": sterilisation,
        "identification": identification,
        "deparasitage": deparasitage,
        "commentaire": commentaire,
        "photo": photo,
        "carousel": carousel
    }
    cursor.execute(
        "INSERT INTO chat (nom, sexe, naissance, race, robe, vaccin, sterilisation,\
         identification, deparasitage, commentaire, photo, carousel) VALUES (%(nom)s, %(sexe)s,%(naissance)s,\
         %(race)s,%(robe)s,%(vaccin)s,%(sterilisation)s,%(identification)s,%(deparasitage)s,%(commentaire)s,\
         %(photo)s,%(carousel)s)",
        new_chat)
    connection.commit()
    cursor.close()
    connection.close()
