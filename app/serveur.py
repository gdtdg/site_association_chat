import os

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from app.connect_bdd import select_one_cat, select_all_cats, insert_message, select_user,\
    insert_chat, select_all_messages, delete_message

app = Flask(__name__)


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


@app.route('/adoptions/')
def adoptions():
    cat_list = select_all_cats()
    cat_list_len = len(cat_list['data'])
    images = os.listdir(os.path.join(app.static_folder, 'adoptions_images'))
    return render_template('adoptions.html', cat_list_len=cat_list_len, cat_list=cat_list, images=images)


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


@app.route('/adoptions/<id_chat>')
def adoption(id_chat):
    my_cat = select_one_cat(id_chat)
    carousel_cat = list(my_cat['carousel'].split(','))
    carousel_cat_len = len(carousel_cat)
    return render_template('fiche_detaillee.html', nom=my_cat['nom'], sexe=my_cat['sexe'],
                           naissance=my_cat['naissance'], race=my_cat['race'], robe=my_cat['robe'],
                           vaccin=my_cat['vaccin'], sterilisation=my_cat['sterilisation'],
                           identification=my_cat['identification'], deparasitage=my_cat['deparasitage'],
                           commentaire=my_cat['commentaire'], photo=my_cat['photo'], carousel_cat_len=carousel_cat_len,
                           carousel_cat=carousel_cat)


@app.route('/adoptions/json')
def adoption_json():
    cat_list = select_all_cats()
    return cat_list


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
    insert_message(nom, prenom, adresse, code_postal, ville, email, telephone,
                   objet, message)
    return render_template('message_contact_envoye.html', nom=nom, prenom=prenom)


session = []


@app.route('/login/', methods=["GET", "POST"])
def login():
    if len(session) != 0:
        return redirect(url_for('profile'))
    current_user = request.form.get("username")
    current_password = request.form.get("password")
    if select_user(current_user, current_password):
        if current_user not in session:
            session.append(current_user)
        return redirect(url_for('profile'))
    return render_template('login.html')


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
    carousel = request.form.get("carousel")
    insert_chat(nom, sexe, naissance, race, robe, vaccin, sterilisation, identification, deparasitage, commentaire,
                photo, carousel)
    return render_template('chat_ajoute.html', nom=nom)


@app.route('/messages_contact/')
def messages_contact():
    if len(session) != 0:
        messages_list = select_all_messages()
        messages_list_len = len(messages_list['data'])
        return render_template('messages_contact.html', messages_list_len=messages_list_len,
                               messages_list=messages_list)
    else:
        return render_template('login.html')

@app.route('/message_supprime/', methods=["POST"])
def message_supprime():
    id_message = request.form.get("id_message")
    delete_message(id_message)
    return render_template('message_supprime.html', id_message=id_message)
