from flask import Blueprint, jsonify, request
from flask_login import login_required

from digicheese import db
from digicheese.decorator.role_required import role_required
from digicheese.repositories import AdresseRepository

colis_adresses = Blueprint("colis_adresses", __name__, url_prefix="/colis/adresses")

repo = AdresseRepository(db.session)


@colis_adresses.route("/", methods=["GET"])
@login_required
@role_required("colis")
def list_adresses():
    """
    Liste toutes les adresses
    ---
    tags:
      - Operateur Colis / Adresses
    responses:
      200:
        description: Liste des adresses
        content:
          application/json:
            example:
              - id: 1
                comp_adresse1: "12 Rue Principale"
                comp_adresse2: "Bâtiment A"
                comp_adresse3: "Appartement 3"
                commune_cp: 34000
              - id: 2
                comp_adresse1: "5 Avenue de la Gare"
                comp_adresse2: ""
                comp_adresse3: ""
                commune_cp: 75001
    """
    adresses = repo.get_all()
    return jsonify([a.to_json() for a in adresses]), 200


@colis_adresses.route("/<int:adresse_id>", methods=["GET"])
@login_required
@role_required("colis")
def get_adresse(adresse_id):
    """
    Récupère une adresse par ID
    ---
    tags:
      - Operateur Colis / Adresses
    parameters:
      - name: adresse_id
        in: path
        required: true
        schema:
          type: integer
        description: ID de l'adresse
    responses:
      200:
        description: Adresse trouvée
        content:
          application/json:
            example:
              id: 1
              comp_adresse1: "12 Rue Principale"
              comp_adresse2: "Bâtiment A"
              comp_adresse3: "Appartement 3"
              commune_cp: 34000
      404:
        description: Adresse non trouvée
    """
    adresse = repo.get_by_id(adresse_id)
    if not adresse:
        return jsonify({"error": "Adresse non trouvée"}), 404

    return jsonify(adresse.to_json()), 200


@colis_adresses.route("/add", methods=["POST"])
@login_required
@role_required("colis")
def add_adresse():
    """
    Ajoute une adresse
    ---
    tags:
      - Operateur Colis / Adresses
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - comp_adresse1
            - commune_cp
          properties:
            comp_adresse1:
              type: string
              example: "12 Rue Principale"
            comp_adresse2:
              type: string
              example: "Bâtiment A"
            comp_adresse3:
              type: string
              example: "Appartement 3"
            commune_cp:
              type: integer
              example: 34000
    responses:
      201:
        description: Adresse créée
      400:
        description: Champs manquants
    """
    data = request.get_json() or {}

    comp_adresse1 = data.get("comp_adresse1")
    comp_adresse2 = data.get("comp_adresse2", "")
    comp_adresse3 = data.get("comp_adresse3", "")
    commune_cp = data.get("commune_cp")

    if not comp_adresse1 or not commune_cp:
        return jsonify({"error": "Champs manquants"}), 400

    adresse = repo.add(
        comp_adresse1=comp_adresse1,
        comp_adresse2=comp_adresse2,
        comp_adresse3=comp_adresse3,
        commune_cp=commune_cp,
    )

    return jsonify({"message": "Adresse créée", "id": adresse.id}), 201


@colis_adresses.route("/update/<int:adresse_id>", methods=["PUT"])
@login_required
@role_required("colis")
def update_adresse(adresse_id):
    """
    Met à jour une adresse
    ---
    tags:
      - Operateur Colis / Adresses
    parameters:
      - name: adresse_id
        in: path
        required: true
        schema:
          type: integer
        description: ID de l'adresse
      - in: body
        name: body
        required: false
        schema:
          type: object
          properties:
            comp_adresse1:
              type: string
              example: "12 Rue Principale"
            comp_adresse2:
              type: string
              example: "Bâtiment A"
            comp_adresse3:
              type: string
              example: "Appartement 3"
            commune_cp:
              type: integer
              example: 34000
    responses:
      200:
        description: Adresse mise à jour
        content:
          application/json:
            example:
              message: "Adresse mise à jour"
              id: 1
      400:
        description: Aucun champ à mettre à jour
      404:
        description: Adresse non trouvée
    """
    data = request.get_json() or {}

    update_data = {}
    for field in ("comp_adresse1", "comp_adresse2", "comp_adresse3", "commune_cp"):
        if field in data:
            update_data[field] = data[field]

    if not update_data:
        return jsonify({"error": "Aucun champ à mettre à jour"}), 400

    adresse = repo.update(adresse_id, **update_data)
    if not adresse:
        return jsonify({"error": "Adresse non trouvée"}), 404

    return jsonify({"message": "Adresse mise à jour", "id": adresse_id}), 200


@colis_adresses.route("/delete/<int:adresse_id>", methods=["DELETE"])
@login_required
@role_required("colis")
def delete_adresse(adresse_id):
    """
    Supprime une adresse
    ---
    tags:
      - Operateur Colis / Adresses
    parameters:
      - name: adresse_id
        in: path
        required: true
        schema:
          type: integer
        description: ID de l'adresse à supprimer
    responses:
      200:
        description: Adresse supprimée
        content:
          application/json:
            example:
              message: "Adresse 1 supprimée"
      404:
        description: Adresse non trouvée
    """
    adresse = repo.get_by_id(adresse_id)
    if not adresse:
        return jsonify({"error": "Adresse non trouvée"}), 404

    repo.delete(adresse_id)
    return jsonify({"message": f"Adresse {adresse_id} supprimée"}), 200
