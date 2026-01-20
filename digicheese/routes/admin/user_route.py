from flask import Blueprint, jsonify, request
from flask_login import login_required

from digicheese.repositories.r_utilisateur import UtilisateurRepository
from digicheese.decorator.role_required import role_required
from digicheese import db
from werkzeug.security import generate_password_hash



admin_users = Blueprint('admin_users',__name__,url_prefix='/admin/users')
repo = UtilisateurRepository(db.session)


@admin_users.route('/', methods=['GET'])
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
    return jsonify([user.to_json() for user in users ]), 200


@admin_users.route('/<int:user_id>', methods=['GET'])
@login_required
@role_required('admin')
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
        return user.to_json(),200
    return jsonify({"error": "Utilisateur non trouvé"}), 404

@admin_users.route('/add', methods=['POST'])
@login_required
@role_required('admin')
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


@admin_users.route('/delete/<int:user_id>', methods=['DELETE'])
@login_required
@role_required('admin')
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
    user = repo.get_by_id(user_id)
    if not user:
        return jsonify({"error": "Utilisateur non trouvé"}), 404

    repo.delete(user_id)
    return jsonify({
        "message": "Utilisateur suprimé",
        "id": user_id
    }), 200

@admin_users.route('/update/<int:user_id>', methods=['PUT'])
@login_required
@role_required('admin')
def update_user(user_id):
    """
    Met un utilisateur à jour
    ---
    tags:
      - Admin / Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID de l'utilisateur à modifier
      - in: body
        name: body
        required: false
        schema:
          type: object
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
      200:
        description: Utilisateur mis à jour
      400:
        description: Aucune donnée valide fournie
      404:
        description: Utilisateur introuvable
    """
    data = request.get_json() or {}

    update_data = {}
    for field in ("email", "name", "password"):
        if field in data and data[field] is not None:
            if field == "password":
                update_data[field] = generate_password_hash(data[field])
            else:
                update_data[field] = data[field]

    if not update_data:
        return jsonify({"error": "Aucun champ à mettre à jour"}), 400

    user = repo.update(user_id, **update_data)
    if user is None:
        return jsonify({"error": "Utilisateur introuvable"}), 404

    return jsonify({
        "message": "Utilisateur mis à jour",
        "id": user_id
    }), 200

