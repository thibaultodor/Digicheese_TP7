from flask import Blueprint, jsonify, request
from flask_login import login_required
from digicheese.repositories.r_utilisateur import UtilisateurRepository
from digicheese.decorator.role_required import role_required
from digicheese import db
from werkzeug.security import generate_password_hash


admin = Blueprint('admin', __name__, url_prefix='/admin')
repo = UtilisateurRepository(db.session)


@admin.route('/users', methods=['GET'])
@login_required
@role_required('admin')
def list_users():
    """
    Liste tous les utilisateurs
    ---
    tags:
      - Admin / Users
    responses:
      200:
        description: Liste des utilisateurs
    """
    users = repo.get_all()

    return jsonify([
        {
            "id": u.id,
            "email": u.email,
            "name": u.name
            } for u in users
    ])


@admin.route('/user/<int:user_id>', methods=['GET'])
@login_required
def get_user(user_id):
    """
    Récupère un utilisateur par ID
    ---
    tags:
      - Admin / Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID de l'utilisateur
    responses:
      200:
        description: Utilisateur trouvé
        content:
          application/json:
            example:
              id: 1
              name: "Julien"
      404:
        description: Utilisateur non trouvé
    """
    user = repo.get_by_id(user_id)
    if user:
        return jsonify([
            {
                "id": user.id,
                "email": user.email,
                "name": user.name
            }
        ])
    return jsonify({"error": "Utilisateur non trouvé"}), 404

@admin.route('/addUser', methods=['POST'])
@login_required
def add_user():
    """
    Ajoute un utilisateur
    ---
    tags:
      - Admin / Users
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - email
            - name
            - password
          properties:
            email:
              type: string
              example: test@mail.com
            name:
              type: string
              example: Julien
            password:
              type: string
              example: secret123
    responses:
      201:
        description: Utilisateur créé
      400:
        description: Données invalides
    """
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')
    password = generate_password_hash(password)
    if not email or not name or not password:
        return jsonify({"error": "Champs manquants"}), 400

    user = repo.add(email=email, name=name, password=password)
    return jsonify({
        "message": "Utilisateur créé",
        "id": user.id
    }), 201





#TODO
@admin.route('/deleteUser/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    """
    Supprime un utilisateur par ID
    ---
    tags:
      - Admin / Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID de l'utilisateur à supprimer
    responses:
      200:
        description: Utilisateur supprimé avec succès
        content:
          application/json:
            example:
              message: "Utilisateur 1 supprimé"
      404:
        description: Utilisateur non trouvé
    """
    return True

#TODO
@admin.route('/updateUser/<int:user_id>', methods=['PUT'])
@login_required
def update_user(user_id):
    """
    Met à jour un utilisateur par ID
    ---
    tags:
      - Admin / Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID de l'utilisateur à modifier
    responses:
      200:
        description: Utilisateur modifié
        content:
          application/json:
            example:
              message: "Utilisateur 1 modifié"
      404:
        description: Utilisateur non trouvé
    """
    return True



#TODO
@admin.route('/objets', methods=['GET'])
@login_required
@role_required('admin')
def list_objets():
    """
    Liste tous les goodies
    ---
    tags:
      - Admin / objet
    responses:
      200:
        description: Liste des goodies
    """
    # repo = UserRepository(db.session)
    # users = repo.get_all()
    return True
    # return jsonify([
    #     {
    #         "id": u.id,
    #         "email": u.email,
    #         "name": u.name
    #         } for u in users
    # ])

#TODO
@admin.route('/objet', methods=['GET'])
@login_required
@role_required('admin')
def objet():
    """
    Recherche un goodie par ID
    ---
    tags:
      - Admin / objet
    responses:
      200:
        description: Recherche un goodie par ID
    """
    # repo = UserRepository(db.session)
    # users = repo.get_all()
    return True
    # return jsonify([
    #     {
    #         "id": u.id,
    #         "email": u.email,
    #         "name": u.name
    #         } for u in users
    # ])

#TODO
@admin.route('/addObjet', methods=['POST'])
@login_required
@role_required('admin')
def add_objet():
    """
    Ajoute un goodie
    ---
    tags:
      - Admin / objet
    responses:
      200:
        description: ajoute un goodie
    """
    return True

#TODO
@admin.route('/updateObjet', methods=['PUT'])
@login_required
@role_required('admin')
def update_objet():
    """
    Met a jour un goodie par ID
    ---
    tags:
      - Admin / objet
    responses:
      200:
        description: Met a jour un goodie par ID
    """
    return True

#TODO
@admin.route('/deleteObjet', methods=['DELETE'])
@login_required
@role_required('admin')
def delete_objet():
    """
    Supprime un goodie par ID
    ---
    tags:
      - Admin / objet
    responses:
      200:
        description: Supprime un goodie par ID
    """
    return True

