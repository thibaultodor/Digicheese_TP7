from flask import Blueprint, jsonify, request
from flask_login import login_required

from digicheese import db
from digicheese.decorator.role_required import role_required
from digicheese.repositories import DetailCommandeRepository

colis_detail_commandes = Blueprint(
    'colis_detail_commandes',
    __name__,
    url_prefix='/colis/detail_commandes'
)

repo = DetailCommandeRepository(db.session)



@colis_detail_commandes.route('/', methods=['GET'])
@login_required
@role_required('colis')
def list_detail_commandes():
    """
    Liste tous les détails de commandes
    ---
    tags:
      - Operateur Colis / Détails Commandes
    responses:
      200:
        description: Liste des détails de commandes
        content:
          application/json:
            example:
              - id: 1
                quantite: 5
                colis: 3
                commentaire: "Fragile"
                commande_id: 1
                objet_id: 2
              - id: 2
                quantite: 2
                colis: 1
                commentaire: ""
                commande_id: 1
                objet_id: 3
    """
    details = repo.get_all()
    return jsonify([d.to_json() for d in details]), 200


@colis_detail_commandes.route('/<int:detail_id>', methods=['GET'])
@login_required
@role_required('colis')
def get_detail_commande(detail_id):
    """
    Récupère un détail de commande par ID
    ---
    tags:
      - Operateur Colis / Détails Commandes
    parameters:
      - name: detail_id
        in: path
        required: true
        schema:
          type: integer
        description: ID du détail de commande
    responses:
      200:
        description: Détail trouvé
        content:
          application/json:
            example:
              id: 1
              quantite: 5
              colis: 3
              commentaire: "Fragile"
              commande_id: 1
              objet_id: 2
      404:
        description: Détail de commande non trouvé
    """
    detail = repo.get_by_id(detail_id)
    if not detail:
        return jsonify({"error": "Détail de commande non trouvé"}), 404

    return jsonify(detail.to_json()), 200


@colis_detail_commandes.route('/add', methods=['POST'])
@login_required
@role_required('colis')
def add_detail_commande():
    """
    Ajoute un détail de commande
    ---
    tags:
      - Operateur Colis / Détails Commandes
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - quantite
            - colis
            - commande_id
            - objet_id
          properties:
            quantite:
              type: integer
              example: 5
            colis:
              type: integer
              example: 3
            commentaire:
              type: string
              example: "Fragile"
            commande_id:
              type: integer
              example: 1
            objet_id:
              type: integer
              example: 2
    responses:
      201:
        description: Détail de commande créé
      400:
        description: Champs manquants
    """
    data = request.get_json() or {}

    quantite = data.get('quantite')
    colis = data.get('colis')
    commentaire = data.get('commentaire', '')
    commande_id = data.get('commande_id')
    objet_id = data.get('objet_id')

    if quantite is None or colis is None or commande_id is None or objet_id is None:
        return jsonify({"error": "Champs manquants"}), 400

    detail = repo.add(
        quantite=quantite,
        colis=colis,
        commentaire=commentaire,
        commande_id=commande_id,
        objet_id=objet_id
    )

    return jsonify({
        "message": "Détail de commande créé",
        "id": detail.id
    }), 201



@colis_detail_commandes.route('/update/<int:detail_id>', methods=['PUT'])
@login_required
@role_required('colis')
def update_detail_commande(detail_id):
    """
    Met à jour un détail de commande
    ---
    tags:
      - Operateur Colis / Détails Commandes
    parameters:
      - name: detail_id
        in: path
        required: true
        schema:
          type: integer
        description: ID du détail de commande
      - in: body
        name: body
        required: false
        schema:
          type: object
          properties:
            quantite:
              type: integer
            colis:
              type: integer
            commentaire:
              type: string
            commande_id:
              type: integer
            objet_id:
              type: integer
    responses:
      200:
        description: Détail de commande mis à jour
        content:
          application/json:
            example:
              message: "Détail de commande mis à jour"
              id: 1
      400:
        description: Aucun champ à mettre à jour
      404:
        description: Détail de commande non trouvé
    """
    data = request.get_json() or {}

    update_data = {}
    for field in ("quantite", "colis", "commentaire", "commande_id", "objet_id"):
        if field in data:
            update_data[field] = data[field]

    if not update_data:
        return jsonify({"error": "Aucun champ à mettre à jour"}), 400

    detail = repo.update(detail_id, **update_data)
    if not detail:
        return jsonify({"error": "Détail de commande non trouvé"}), 404

    return jsonify({
        "message": "Détail de commande mis à jour",
        "id": detail_id
    }), 200




@colis_detail_commandes.route('/delete/<int:detail_id>', methods=['DELETE'])
@login_required
@role_required('colis')
def delete_detail_commande(detail_id):
    """
    Supprime un détail de commande
    ---
    tags:
      - Operateur Colis / Détails Commandes
    parameters:
      - name: detail_id
        in: path
        required: true
        schema:
          type: integer
        description: ID du détail de commande à supprimer
    responses:
      200:
        description: Détail de commande supprimé
        content:
          application/json:
            example:
              message: "Détail de commande 1 supprimé"
      404:
        description: Détail de commande non trouvé
    """
    detail = repo.get_by_id(detail_id)
    if not detail:
        return jsonify({"error": "Détail de commande non trouvé"}), 404

    repo.delete(detail_id)
    return jsonify({
        "message": f"Détail de commande {detail_id} supprimé"
    }), 200
