from flask import Blueprint, jsonify
from flask_login import login_required

from digicheese.decorator.role_required import role_required

admin = Blueprint('admin', __name__, url_prefix='/admin')

# Liste de test d'utilisateurs
fake_users = [
    {"id": 1, "name": "Julien"},
    {"id": 2, "name": "Alice"},
    {"id": 3, "name": "Bob"}
]

@admin.route('/users')
@login_required
@role_required('colis')
def list_users():
    """
    Liste tous les utilisateurs
    ---
    tags:
      - Admin
    responses:
      200:
        description: Liste des utilisateurs
        content:
          application/json:
            example:
              - id: 1
                name: "Julien"
              - id: 2
                name: "Alice"
    """
    return jsonify(fake_users)


@admin.route('/user/<int:user_id>')
@login_required
def get_user(user_id):
    """
    Récupère un utilisateur par ID
    ---
    tags:
      - Admin
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
    user = next((u for u in fake_users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "Utilisateur non trouvé"}), 404


@admin.route('/deleteUser/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    """
    Supprime un utilisateur par ID
    ---
    tags:
      - Admin
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
    global fake_users
    user = next((u for u in fake_users if u["id"] == user_id), None)
    if user:
        fake_users = [u for u in fake_users if u["id"] != user_id]
        return jsonify({"message": f"Utilisateur {user_id} supprimé"})
    return jsonify({"error": "Utilisateur non trouvé"}), 404


@admin.route('/updateUser/<int:user_id>', methods=['PUT'])
@login_required
def update_user(user_id):
    """
    Met à jour un utilisateur par ID
    ---
    tags:
      - Admin
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
    user = next((u for u in fake_users if u["id"] == user_id), None)
    if user:
        # Exemple de modification aléatoire pour test
        user["name"] = user["name"] + "_updated"
        return jsonify({"message": f"Utilisateur {user_id} modifié"})
    return jsonify({"error": "Utilisateur non trouvé"}), 404
