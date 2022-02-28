import os
from functools import wraps

from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user, login_required, logout_user, utils, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from app.app import login_manager, app, db, db_insert, db_delete, save_image
from app.models.Chat import Chat
from app.models.MessageContact import MessageContact
from app.models.Role import Role
from app.models.User import User
from app.models.UserRoles import UserRoles

# test des branches

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def role_required(role_name):
    def admin_required(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            current_user = utils.current_user
            if not current_user.is_authenticated:
                return app.login_manager.unauthorized()
            else:
                user_roles_id = UserRoles.query.filter_by(user_id=current_user.id).all()
                roles = [Role.query.filter_by(id=user_role_id.role_id).first() for user_role_id in user_roles_id]
                if any(role.name == role_name for role in roles):
                    return func(*args, **kwargs)
            return app.login_manager.unauthorized()

        return decorated_view

    return admin_required



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
    carousel_cat_len = len(carousel_cat)  # Obligé de garder cette variable pour que le carousel fonctionne.
    # Sinon la class 'carousel-item active' bloque le carousel.
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
    db_insert(message_insert)
    return render_template('message_contact_envoye.html', message_insert=message_insert)


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/login_post/', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("L'utilisateur ou le mot de passe est invalide.")
        return redirect(url_for('login'))
    login_user(user, remember=remember)
    return redirect(url_for('profile'))


@app.route('/signup/')
def signup():
    return render_template('signup.html')


@app.route('/signup_post/', methods=["POST"])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if user:
        flash("L'adresse email existe déjà.")
        return redirect(url_for('signup'))
    new_user = User(email=email, name=name, password=generate_password_hash(password))
    db_insert(new_user)
    # For every new user we add a guest role in UserRoles table:
    new_user_role = UserRoles(user_id=new_user.id, role_id='2')
    db_insert(new_user_role)
    return render_template('compte_cree.html', name=name)


@app.route('/profile/')
@login_required
def profile():
    # To show the role (1 or 2) in the html template:
    role = db.session.query(UserRoles).filter_by(user_id=current_user.id).first()
    return render_template('profile.html', role=role.role_id)


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return render_template('logout.html')


@app.route('/ajouter_chat/')
@login_required
@role_required('Admin')
def ajouter_chat():
    return render_template('ajouter_chat.html')


@app.route('/chat_ajoute/', methods=["POST"])
@login_required
@role_required('Admin')
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

    photo = request.files.get('photo')
    carousel = request.files.getlist('carousel')
    carousel = [file for file in carousel if file.mimetype != 'application/octet-stream']
    if photo.mimetype != 'application/octet-stream':
        carousel.insert(0, photo)

    photo_path = ''
    carousel_paths = ''
    try:
        photo_path = secure_filename(photo.filename)
        # We want a string of images name separated by ',':
        carousel_paths = ','.join(secure_filename(file.filename) for file in carousel)
    except Exception:
        print('No cat pictures')

    chat_insert = Chat(nom=nom, sexe=sexe, naissance=naissance,
                       race=race, robe=robe, vaccin=vaccin,
                       sterilisation=sterilisation, identification=identification,
                       deparasitage=deparasitage, commentaire=commentaire,
                       photo=photo_path, carousel=carousel_paths)
    db_insert(chat_insert)

    # save carousel
    for image in carousel:
        save_image(image)

    return render_template('chat_ajoute.html', chat_insert=chat_insert)


@app.route('/messages_contact/')
@login_required
@role_required('Admin')
def messages_contact():
    messages_list = db.session.query(MessageContact).all()
    return render_template('messages_contact.html', messages_list=messages_list)


@app.route('/message_supprime/', methods=["POST"])
@login_required
@role_required('Admin')
def message_supprime():
    id_message = request.form.get("id_message")
    message_delete = db.session.query(MessageContact).filter_by(id=id_message).first()
    db_delete(message_delete)
    return render_template('message_supprime.html', message_delete=message_delete)
