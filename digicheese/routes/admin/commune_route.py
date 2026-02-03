"""Admin routes for commune management."""

from flask import Blueprint, jsonify, request
from flask_login import login_required

from digicheese import db
from digicheese.decorator.role_required import role_required
from digicheese.repositories import CommuneRepository

admin_communes = Blueprint(
    "admin_communes", __name__, url_prefix="/admin/communes"
)

repo = CommuneRepository(db.session)


@admin_communes.route("/", methods=["GET"])
@login_required
@role_required("admin")
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
              - cp: "34000"
                commune: "Montpellier"
                departement: "Hérault"
              - cp: "75001"
                commune: "Paris"
                departement: "Paris"
    """
    communes = repo.get_all()
    return jsonify([commune.to_json() for commune in communes]), 200


@admin_communes.route("/<string:cp>", methods=["GET"])
@login_required
@role_required("admin")
def get_commune(cp):
    """
    Récupère une commune par code postal
    ---
    tags:
      - Admin / Communes
    parameters:
      - name: cp
        in: path
        required: true
        schema:
          type: string
        description: Code postal de la commune
    responses:
      200:
        description: Commune trouvée
        content:
          application/json:
            example:
              cp: "34000"
              commune: "Montpellier"
              departement: "Hérault"
      404:
        description: Commune non trouvée
    """
    commune = repo.get_by_id(cp)
    if not commune:
        return jsonify({"error": "Commune non trouvée"}), 404

    return commune.to_json(), 200


@admin_communes.route("/add", methods=["POST"])
@login_required
@role_required("admin")
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
              cp: "34000"
      400:
        description: Données invalides
    """
    data = request.get_json() or {}

    cp = data.get("cp")
    commune_name = data.get("commune")
    departement = data.get("departement")

    if not cp or not commune_name or not departement:
        return jsonify({"error": "Champs manquants"}), 400

    commune = repo.add(cp=cp, commune=commune_name, departement=departement)

    return jsonify({"message": "Commune créée", "cp": commune.cp}), 201


@admin_communes.route("/delete/<string:cp>", methods=["DELETE"])
@login_required
@role_required("admin")
def delete_commune(cp):
    """
    Supprime une commune par code postal
    ---
    tags:
      - Admin / Communes
    parameters:
      - name: cp
        in: path
        required: true
        schema:
          type: string
        description: Code postal de la commune à supprimer
    responses:
      200:
        description: Commune supprimée
        content:
          application/json:
            example:
              message: "Commune 34000 supprimée"
      404:
        description: Commune non trouvée
    """
    commune = repo.get_by_id(cp)
    if not commune:
        return jsonify({"error": "Commune non trouvée"}), 404

    repo.delete(cp)
    return jsonify({"message": f"Commune {cp} supprimée"}), 200


@admin_communes.route("/update/<string:cp>", methods=["PUT"])
@login_required
@role_required("admin")
def update_commune(cp):
    """
    Met à jour une commune (sans modifier le CP)
    ---
    tags:
      - Admin / Communes
    parameters:
      - name: cp
        in: path
        type: string
        required: true
        description: Code postal de la commune
      - in: body
        name: body
        required: false
        schema:
          type: object
          properties:
            commune:
              type: string
              example: "Montpellier"
            departement:
              type: string
              example: "Hérault"
    responses:
      200:
        description: Commune mise à jour
      400:
        description: Aucun champ à mettre à jour
      404:
        description: Commune introuvable
    """
    data = request.get_json() or {}

    update_data = {}
    for field in ("commune", "departement"):
        if field in data:
            update_data[field] = data[field]

    if not update_data:
        return jsonify({"error": "Aucun champ à mettre à jour"}), 400

    commune = repo.update(cp, **update_data)
    if not commune:
        return jsonify({"error": "Commune introuvable"}), 404

    return jsonify({"message": "Commune mise à jour", "cp": cp}), 200
