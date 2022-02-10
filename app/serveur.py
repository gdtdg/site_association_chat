import os

from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from app.orm_insert_delete import insert, delete
from app.orm_tables import db, app, Chat, MessageContact, User


@app.route('/')
def root():
    return redirect(url_for('index'))


@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/header/')
def header():
    return render_template('header.html')


@app.route('/footer/')
def footer():
    return render_template('footer.html')


@app.route('/association/')
def association():
    return render_template('association.html')


@app.route('/actualites/')
def actualites():
    return render_template('login.html')


@app.route('/soutenir/')
def soutenir():
    return render_template('soutenir.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/a_propos/')
def a_propos():
    return render_template('a_propos.html')


@app.route('/adoptions/')
def adoptions():
    cat_list = db.session.query(Chat).all()
    images = os.listdir(os.path.join(app.static_folder, 'adoptions_images'))
    return render_template('adoptions.html', cat_list=cat_list, images=images)


@app.route('/adoptions/<id_chat>')
def adoption(id_chat):
    my_cat = db.session.query(Chat).filter_by(id=id_chat).first()
    carousel_cat = list(my_cat.carousel.split(','))
    carousel_cat_len = len(carousel_cat)
    return render_template('fiche_detaillee.html', my_cat=my_cat, carousel_cat_len=carousel_cat_len,
                           carousel_cat=carousel_cat)


@app.route('/form/', methods=["POST"])
def form():
    nom = request.form.get("nom")
    prenom = request.form.get("prenom")
    adresse = request.form.get("adresse")
    code_postal = request.form.get("code_postal")
    ville = request.form.get("ville")
    email = request.form.get("email")
    telephone = request.form.get("telephone")
    objet = request.form.get("objet")
    message = request.form.get("message")
    message_insert = MessageContact(nom=nom, prenom=prenom, adresse=adresse,
                                    code_postal=code_postal, ville=ville, email=email,
                                    telephone=telephone, objet=objet, message=message)
    insert(message_insert)
    return render_template('message_contact_envoye.html', message_insert=message_insert)


session = []


@app.route('/login/', methods=["GET"])
def login():
    if len(session) != 0:
        return redirect(url_for('profile'))
    return render_template('login.html')


@app.route('/login/', methods=["POST"])
def login_post():
    current_user = request.form.get("username")
    current_password = request.form.get("password")
    if db.session.query(User).filter_by(username=current_user).filter_by(password=current_password).first():
        if current_user not in session:
            session.append(current_user)
        return redirect(url_for('profile'))
    return redirect(url_for('login'))


@app.route('/profile/')
def profile():
    if len(session) != 0:
        return render_template('profile.html')
    else:
        return render_template('login.html')


@app.route('/logout/')
def logout():
    session.clear()
    return render_template('logout.html')


@app.route('/ajouter_chat/')
def ajouter_chat():
    if len(session) != 0:
        return render_template('ajouter_chat.html')
    else:
        return render_template('login.html')


@app.route('/chat_ajoute/', methods=["POST"])
def chat_ajoute():
    nom = request.form.get("nom")
    sexe = request.form.get("sexe")
    naissance = request.form.get("naissance")
    race = request.form.get("race")
    robe = request.form.get("robe")
    vaccin = request.form.get("vaccin")
    sterilisation = request.form.get("sterilisation")
    identification = request.form.get("identification")
    deparasitage = request.form.get("deparasitage")
    commentaire = request.form.get("commentaire")
    photo = request.form.get("photo")
    carousel = request.form.getlist("carousel")
    chat_insert = Chat(nom=nom, sexe=sexe, naissance=naissance,
                       race=race, robe=robe, vaccin=vaccin,
                       sterilisation=sterilisation, identification=identification,
                       deparasitage=deparasitage, commentaire=commentaire,
                       photo=photo, carousel=carousel)
    insert(chat_insert)
    return render_template('chat_ajoute.html', chat_insert=chat_insert)


@app.route('/messages_contact/')
def messages_contact():
    if len(session) != 0:
        messages_list = db.session.query(MessageContact).all()
        return render_template('messages_contact.html', messages_list=messages_list)
    else:
        return render_template('login.html')


@app.route('/message_supprime/', methods=["POST"])
def message_supprime():
    id_message = request.form.get("id_message")
    message_delete = db.session.query(MessageContact).filter_by(id=id_message).first()
    delete(message_delete)
    return render_template('message_supprime.html', message_delete=message_delete)
