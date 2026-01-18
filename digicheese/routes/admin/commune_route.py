from flask import Blueprint, jsonify, request
from flask_login import login_required

from digicheese import db
from digicheese.decorator.role_required import role_required
from digicheese.repositories import CommuneRepository

admin_communes = Blueprint('admin_communes', __name__, url_prefix='/admin/communes')
repo = CommuneRepository(db.session)

@admin_communes.route('/', methods=['GET'])
@login_required
@role_required('admin')
def list_communes():
    """
    Liste toutes les communes
    ---
    tags:
      - Admin / Communes
    responses:
      200:
        description: Liste des communes
        content:
          application/json:
            example:
              - id: 1
                cp: "34000"
                commune: "Montpellier"
                departement: "Hérault"
              - id: 2
                cp: "75001"
                commune: "Paris"
                departement: "Paris"
    """
    communes = repo.get_all()
    return jsonify([
        {
            "id": c.id,
            "cp": c.cp,
            "commune": c.commune,
            "departement": c.departement
        }
        for c in communes
    ])


@admin_communes.route('/<int:commune_id>', methods=['GET'])
@login_required
@role_required('admin')
def get_commune(commune_id):
    """
    Récupère une commune par ID
    ---
    tags:
      - Admin / Communes
    parameters:
      - name: commune_id
        in: path
        type: integer
        required: true
        description: ID de la commune à récupérer
    responses:
      200:
        description: Commune trouvée
        content:
          application/json:
            example:
              id: 1
              cp: "34000"
              commune: "Montpellier"
              departement: "Hérault"
      404:
        description: Commune non trouvée
    """
    commune = repo.get_by_id(commune_id)
    if not commune:
        return jsonify({"error": "Commune non trouvée"}), 404

    return jsonify({
        "cp": commune.cp,
        "commune": commune.commune,
        "departement": commune.departement
    })


@admin_communes.route('/add', methods=['POST'])
@login_required
@role_required('admin')
def add_commune():
    """
    Ajoute une commune
    ---
    tags:
      - Admin / Communes
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - cp
            - commune
            - departement
          properties:
            cp:
              type: string
              example: "34000"
            commune:
              type: string
              example: "Montpellier"
            departement:
              type: string
              example: "Hérault"
    responses:
      201:
        description: Commune créée
        content:
          application/json:
            example:
              message: "Commune créée"
              id: 1
      400:
        description: Données invalides
    """
    data = request.get_json() or {}
    cp = data.get('cp')
    commune_name = data.get('commune')
    departement = data.get('departement')

    if not cp or not commune_name or not departement:
        return jsonify({"error": "Champs manquants"}), 400

    commune = repo.add(cp=cp, commune=commune_name, departement=departement)

    return jsonify({
        "message": "Commune créée",
        "id": commune.id
    }), 201


@admin_communes.route('/delete/<int:commune_id>', methods=['DELETE'])
@login_required
@role_required('admin')
def delete_commune(commune_id):
    """
    Supprime une commune par ID
    ---
    tags:
      - Admin / Communes
    parameters:
      - name: commune_id
        in: path
        type: integer
        required: true
        description: ID de la commune à supprimer
    responses:
      200:
        description: Commune supprimée
        content:
          application/json:
            example:
              message: "Commune 1 supprimée"
      404:
        description: Commune non trouvée
    """
    commune = repo.get_by_id(commune_id)
    if not commune:
        return jsonify({"error": "Commune non trouvée"}), 404

    repo.delete(commune_id)
    return jsonify({
        "message": f"Commune {commune_id} supprimée"
    }), 200


@admin_communes.route('/update/<int:commune_id>', methods=['PUT'])
@login_required
@role_required('admin')
def update_commune(commune_id):
    """
    Met une commune à jour
    ---
    tags:
      - Admin / Communes
    parameters:
      - name: commune_id
        in: path
        type: integer
        required: true
        description: ID de la commune à modifier
      - in: body
        name: body
        required: false
        schema:
          type: object
          properties:
            cp:
              type: string
              example: "34000"
            commune:
              type: string
              example: "Montpellier"
            departement:
              type: string
              example: "Hérault"
    responses:
      200:
        description: Commune mise à jour
        content:
          application/json:
            example:
              message: "Commune mise à jour"
              id: 1
      400:
        description: Aucun champ à mettre à jour
      404:
        description: Commune introuvable
    """
    data = request.get_json() or {}

    update_data = {}
    for field in ("cp", "commune", "departement"):
        if field in data:
            update_data[field] = data[field]

    if not update_data:
        return jsonify({"error": "Aucun champ à mettre à jour"}), 400

    commune = repo.update(commune_id, **update_data)
    if not commune:
        return jsonify({"error": "Commune introuvable"}), 404

    return jsonify({
        "message": "Commune mise à jour",
        "id": commune_id
    }), 200
