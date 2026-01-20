from flask import Blueprint, jsonify, request
from flask_login import login_required

from digicheese import db
from digicheese.decorator.role_required import role_required
from digicheese.repositories import ConditionnementRepository

admin_conditionnements = Blueprint('admin_conditionnements',__name__,url_prefix='/admin/conditionnements')

repo = ConditionnementRepository(db.session)


@admin_conditionnements.route('/', methods=['GET'])
@login_required
@role_required('admin')
def list_conditionnements():
    """
    Liste tous les conditionnements
    ---
    tags:
      - Admin / Conditionnements
    responses:
      200:
        description: Liste des conditionnements
        content:
          application/json:
            example:
              - id: 1
                libelle: "Carton"
                poids_condit: 2.5
                ordre_imp: 1
              - id: 2
                libelle: "Palette"
                poids_condit: 15
                ordre_imp: 2
    """
    conditionnements = repo.get_all()
    return jsonify([c.to_json() for c in conditionnements]), 200



@admin_conditionnements.route('/<int:conditionnement_id>', methods=['GET'])
@login_required
@role_required('admin')
def get_conditionnement(conditionnement_id):
    """
    Récupère un conditionnement par ID
    ---
    tags:
      - Admin / Conditionnements
    parameters:
      - name: conditionnement_id
        in: path
        required: true
        schema:
          type: integer
        description: ID du conditionnement
    responses:
      200:
        description: Conditionnement trouvé
        content:
          application/json:
            example:
              id: 1
              libelle: "Carton"
              poids_condit: 2.5
              ordre_imp: 1
      404:
        description: Conditionnement non trouvé
    """
    conditionnement = repo.get_by_id(conditionnement_id)
    if not conditionnement:
        return jsonify({"error": "Conditionnement non trouvé"}), 404

    return jsonify(conditionnement.to_json()),200


@admin_conditionnements.route('/add', methods=['POST'])
@login_required
@role_required('admin')
def add_conditionnement():
    """
    Ajoute un conditionnement
    ---
    tags:
      - Admin / Conditionnements
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - libelle
            - poids_condit
            - ordre_imp
          properties:
            libelle:
              type: string
              example: "Carton"
            poids_condit:
              type: number
              example: 2.5
            ordre_imp:
              type: integer
              example: 1
    responses:
      201:
        description: Conditionnement créé
      400:
        description: Données invalides
    """
    data = request.get_json() or {}

    libelle = data.get('libelle')
    poids_condit = data.get('poids_condit')
    ordre_imp = data.get('ordre_imp')

    if libelle is None or poids_condit is None or ordre_imp is None:
        return jsonify({"error": "Champs manquants"}), 400

    conditionnement = repo.add(
        libelle=libelle,
        poids_condit=poids_condit,
        ordre_imp=ordre_imp
    )

    return jsonify({
        "message": "Conditionnement créé",
        "id": conditionnement.id
    }), 201


@admin_conditionnements.route('/delete/<int:conditionnement_id>', methods=['DELETE'])
@login_required
@role_required('admin')
def delete_conditionnement(conditionnement_id):
    """
    Supprime un conditionnement
    ---
    tags:
      - Admin / Conditionnements
    parameters:
      - name: conditionnement_id
        in: path
        required: true
        schema:
          type: integer
        description: ID du conditionnement à supprimer
    responses:
      200:
        description: Conditionnement supprimé
        content:
          application/json:
            example:
              message: "Conditionnement 1 supprimé"
      404:
        description: Conditionnement non trouvé
    """
    conditionnement = repo.get_by_id(conditionnement_id)
    if not conditionnement:
        return jsonify({"error": "Conditionnement non trouvé"}), 404

    repo.delete(conditionnement_id)
    return jsonify({
        "message": f"Conditionnement {conditionnement_id} supprimé"
    }), 200



@admin_conditionnements.route('/update/<int:conditionnement_id>', methods=['PUT'])
@login_required
@role_required('admin')
def update_conditionnement(conditionnement_id):
    """
    Met à jour un conditionnement
    ---
    tags:
      - Admin / Conditionnements
    parameters:
      - name: conditionnement_id
        in: path
        required: true
        schema:
          type: integer
        description: ID du conditionnement à modifier
    requestBody:
      required: false
      content:
        application/json:
          schema:
            type: object
            properties:
              libelle:
                type: string
                example: "Carton renforcé"
              poids_condit:
                type: number
                example: 3.0
              ordre_imp:
                type: integer
                example: 1
    responses:
      200:
        description: Conditionnement mis à jour
        content:
          application/json:
            example:
              message: "Conditionnement mis à jour"
              id: 1
      400:
        description: Aucun champ à mettre à jour
      404:
        description: Conditionnement introuvable
    """
    data = request.get_json() or {}

    update_data = {}
    for field in ("libelle", "poids_condit", "ordre_imp"):
        if field in data:
            update_data[field] = data[field]

    if not update_data:
        return jsonify({"error": "Aucun champ à mettre à jour"}), 400

    conditionnement = repo.update(conditionnement_id, **update_data)
    if not conditionnement:
        return jsonify({"error": "Conditionnement introuvable"}), 404

    return jsonify({
        "message": "Conditionnement mis à jour",
        "id": conditionnement_id
    }), 200
