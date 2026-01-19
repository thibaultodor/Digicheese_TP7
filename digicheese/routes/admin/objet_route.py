from flask import Blueprint, jsonify, request
from flask_login import login_required

from digicheese.decorator.role_required import role_required
from digicheese.models import Objet
from digicheese.repositories import ObjetRepository
from digicheese import db
from digicheese.repositories.base_repository import BaseRepository

admin_objets = Blueprint('admin_objets', __name__, url_prefix='/admin/objets')
# repo = ObjetRepository(db.session)
repo = BaseRepository(Objet, db.session)

#appel to json dans les models
@admin_objets.route('/', methods=['GET'])
@login_required
@role_required('admin')
def list_objets():
    """
    Liste tous les objets
    ---
    tags:
      - Admin / Objets
    responses:
      200:
        description: Liste des objets
        content:
          application/json:
            example:
              - id: 1
                libelle: "Épée"
                taille: "M"
                poids: 5
                bl_indispo: false
              - id: 2
                libelle: "Bouclier"
                taille: "L"
                poids: 8
                bl_indispo: true
    """
    objets = repo.get_all()
    return jsonify([o.to_json() for o in objets]), 200


@admin_objets.route('/<int:objet_id>', methods=['GET'])
@login_required
@role_required('admin')
def get_objet(objet_id):
    """
    Récupère un objet par ID
    ---
    tags:
      - Admin / Objets
    parameters:
      - name: objet_id
        in: path
        type: integer
        required: true
        description: ID de l'objet à récupérer
    responses:
      200:
        description: Objet trouvé
        content:
          application/json:
            example:
              id: 1
              libelle: "Épée"
              taille: "M"
              poids: 5
              bl_indispo: false
      404:
        description: Objet non trouvé
    """
    objet = repo.get_by_id(objet_id)
    if not objet:
        return jsonify({"error": "Objet non trouvé"}), 404
    return objet.to_json()


@admin_objets.route('/add', methods=['POST'])
@login_required
@role_required('admin')
def add_objet():
    """
    Ajoute un objet
    ---
    tags:
      - Admin / Objets
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - libelle
            - taille
            - poids
          properties:
            libelle:
              type: string
              example: "Épée"
            taille:
              type: string
              example: "M"
            poids:
              type: integer
              example: 5
            bl_indispo:
              type: boolean
              example: false
    responses:
      201:
        description: Objet créé
        content:
          application/json:
            example:
              message: "Objet créé"
              id: 1
      400:
        description: Données invalides
    """
    data = request.get_json() or {}

    libelle = data.get('libelle')
    taille = data.get('taille')
    poids = data.get('poids')
    bl_indispo = data.get('bl_indispo', False)

    if not libelle or not taille or poids is None:
        return jsonify({"error": "Champs manquants"}), 400

    objet = repo.add(libelle=libelle, taille=taille, poids=poids, bl_indispo=bl_indispo)

    return jsonify({
        "message": "Objet créé",
        "id": objet.id
    }), 201


@admin_objets.route('/delete/<int:objet_id>', methods=['DELETE'])
@login_required
@role_required('admin')
def delete_objet(objet_id):
    """
    Supprime un objet par ID
    ---
    tags:
      - Admin / Objets
    parameters:
      - name: objet_id
        in: path
        type: integer
        required: true
        description: ID de l'objet à supprimer
    responses:
      200:
        description: Objet supprimé avec succès
        content:
          application/json:
            example:
              message: "Objet 1 supprimé"
      404:
        description: Objet non trouvé
    """
    objet = repo.get_by_id(objet_id)
    if not objet:
        return jsonify({"error": "Objet non trouvé"}), 404

    repo.delete(objet_id)
    return jsonify({
        "message": f"Objet {objet_id} supprimé"
    }), 200


@admin_objets.route('/update/<int:objet_id>', methods=['PUT'])
@login_required
@role_required('admin')
def update_objet(objet_id):
    """
    Met un objet à jour
    ---
    tags:
      - Admin / Objets
    parameters:
      - name: objet_id
        in: path
        type: integer
        required: true
        description: ID de l'objet à modifier
      - in: body
        name: body
        required: false
        schema:
          type: object
          properties:
            libelle:
              type: string
              example: "Épée"
            taille:
              type: string
              example: "M"
            poids:
              type: integer
              example: 5
            bl_indispo:
              type: boolean
              example: true
    responses:
      200:
        description: Objet mis à jour
        content:
          application/json:
            example:
              message: "Objet mis à jour"
              id: 1
      400:
        description: Aucune donnée valide fournie
      404:
        description: Objet introuvable
    """
    data = request.get_json() or {}

    update_data = {}
    for field in ("libelle", "taille", "poids", "bl_indispo"):
        if field in data:
            update_data[field] = data[field]

    if not update_data:
        return jsonify({"error": "Aucun champ à mettre à jour"}), 400

    objet = repo.update(objet_id, **update_data)
    if not objet:
        return jsonify({"error": "Objet introuvable"}), 404

    return jsonify({
        "message": "Objet mis à jour",
        "id": objet_id
    }), 200
