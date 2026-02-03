from flask import Blueprint, jsonify, request
from flask_login import login_required

from digicheese import db
from digicheese.decorator.role_required import role_required
from digicheese.repositories import CommandeRepository

colis_commandes = Blueprint("colis_commandes", __name__, url_prefix="/colis/commandes")

repo = CommandeRepository(db.session)


@colis_commandes.route("/", methods=["GET"])
@login_required
@role_required("colis")
def list_commandes():
    """
    Liste toutes les commandes
    ---
    tags:
      - Operateur Colis / Commandes
    responses:
      200:
        description: Liste des commandes
        content:
          application/json:
            example:
              - id: 1
                date: "2024-10-01"
                timbre_client: 12.5
                nb_colis: 3
                b_archive: false
                client_id: 2
                conditionnement_id: 1
    """
    commandes = repo.get_all()
    return jsonify([c.to_json() for c in commandes]), 200


@colis_commandes.route("/<int:commande_id>", methods=["GET"])
@login_required
@role_required("colis")
def get_commande(commande_id):
    """
    Récupère une commande par ID
    ---
    tags:
      - Operateur Colis / Commandes
    parameters:
      - name: commande_id
        in: path
        required: true
        schema:
          type: integer
        description: ID de la commande
    responses:
      200:
        description: Commande trouvée
        content:
          application/json:
            example:
              id: 1
              date: "2024-10-01"
              timbre_client: 12.5
              nb_colis: 3
              b_archive: false
              client_id: 2
              conditionnement_id: 1
      404:
        description: Commande non trouvée
    """
    commande = repo.get_by_id(commande_id)
    if not commande:
        return jsonify({"error": "Commande non trouvée"}), 404

    return jsonify(commande.to_json()), 200


@colis_commandes.route("/add", methods=["POST"])
@login_required
@role_required("colis")
def add_commande():
    """
    Ajoute une commande
    ---
    tags:
      - Operateur Colis / Commandes
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - date
            - timbre_client
            - nb_colis
            - client_id
            - conditionnement_id
          properties:
            date:
              type: string
              format: date
              example: "2024-10-01"
            timbre_client:
              type: number
              example: 12.5
            nb_colis:
              type: integer
              example: 3
            b_archive:
              type: boolean
              example: false
            client_id:
              type: integer
              example: 2
            conditionnement_id:
              type: integer
              example: 1
    responses:
      201:
        description: Commande créée
      400:
        description: Champs manquants
    """
    data = request.get_json() or {}

    date = data.get("date")
    timbre_client = data.get("timbre_client")
    nb_colis = data.get("nb_colis")
    b_archive = data.get("b_archive", False)
    client_id = data.get("client_id")
    conditionnement_id = data.get("conditionnement_id")

    if (
        date is None
        or timbre_client is None
        or nb_colis is None
        or client_id is None
        or conditionnement_id is None
    ):
        return jsonify({"error": "Champs manquants"}), 400

    commande = repo.add(
        date=date,
        timbre_client=timbre_client,
        nb_colis=nb_colis,
        b_archive=b_archive,
        client_id=client_id,
        conditionnement_id=conditionnement_id,
    )

    return jsonify({"message": "Commande créée", "id": commande.id}), 201


@colis_commandes.route("/update/<int:commande_id>", methods=["PUT"])
@login_required
@role_required("colis")
def update_commande(commande_id):
    """
    Met à jour une commande
    ---
    tags:
      - Operateur Colis / Commandes
    parameters:
      - name: commande_id
        in: path
        required: true
        schema:
          type: integer
        description: ID de la commande
      - in: body
        name: body
        required: false
        schema:
          type: object
          properties:
            date:
              type: string
              format: date
            timbre_client:
              type: number
            nb_colis:
              type: integer
            b_archive:
              type: boolean
            client_id:
              type: integer
            conditionnement_id:
              type: integer
    responses:
      200:
        description: Commande mise à jour
        content:
          application/json:
            example:
              message: "Commande mise à jour"
              id: 1
      400:
        description: Aucun champ à mettre à jour
      404:
        description: Commande non trouvée
    """
    data = request.get_json() or {}

    update_data = {}
    for field in (
        "date",
        "timbre_client",
        "nb_colis",
        "b_archive",
        "client_id",
        "conditionnement_id",
    ):
        if field in data:
            update_data[field] = data[field]

    if not update_data:
        return jsonify({"error": "Aucun champ à mettre à jour"}), 400

    commande = repo.update(commande_id, **update_data)
    if not commande:
        return jsonify({"error": "Commande non trouvée"}), 404

    return jsonify({"message": "Commande mise à jour", "id": commande_id}), 200


@colis_commandes.route("/delete/<int:commande_id>", methods=["DELETE"])
@login_required
@role_required("colis")
def delete_commande(commande_id):
    """
    Supprime une commande
    ---
    tags:
      - Operateur Colis / Commandes
    parameters:
      - name: commande_id
        in: path
        required: true
        schema:
          type: integer
        description: ID de la commande à supprimer
    responses:
      200:
        description: Commande supprimée
        content:
          application/json:
            example:
              message: "Commande 1 supprimée"
      404:
        description: Commande non trouvée
    """
    commande = repo.get_by_id(commande_id)
    if not commande:
        return jsonify({"error": "Commande non trouvée"}), 404

    repo.delete(commande_id)
    return jsonify({"message": f"Commande {commande_id} supprimée"}), 200
