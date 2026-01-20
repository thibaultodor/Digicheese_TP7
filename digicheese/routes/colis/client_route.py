from flask import Blueprint, jsonify, request
from flask_login import login_required

from digicheese import db
from digicheese.decorator.role_required import role_required
from digicheese.repositories import ClientRepository


colis_clients = Blueprint(
    'colis_clients',
    __name__,
    url_prefix='/colis/clients'
)

repo = ClientRepository(db.session)



@colis_clients.route('/', methods=['GET'])
@login_required
@role_required('colis')
def list_clients():
    """
    Liste tous les clients
    ---
    tags:
      - Operateur Colis / Clients
    responses:
      200:
        description: Liste des clients
        content:
          application/json:
            example:
              - id: 1
                email_client: "client@test.com"
                adresse_id: 3
              - id: 2
                email_client: "client2@test.com"
                adresse_id: 5
    """
    clients = repo.get_all()
    return jsonify([c.to_json() for c in clients]), 200


@colis_clients.route('/<int:client_id>', methods=['GET'])
@login_required
@role_required('colis')
def get_client(client_id):
    """
    Récupère un client par ID
    ---
    tags:
      - Operateur Colis / Clients
    parameters:
      - name: client_id
        in: path
        required: true
        schema:
          type: integer
        description: ID du client
    responses:
      200:
        description: Client trouvé
        content:
          application/json:
            example:
              id: 1
              email_client: "client@test.com"
              adresse_id: 3
      404:
        description: Client non trouvé
    """
    client = repo.get_by_id(client_id)
    if not client:
        return jsonify({"error": "Client non trouvé"}), 404

    return jsonify(client.to_json()), 200


@colis_clients.route('/add', methods=['POST'])
@login_required
@role_required('colis')
def add_client():
    """
    Ajoute un client
    ---
    tags:
      - Operateur Colis / Clients
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - email_client
            - adresse_id
          properties:
            email_client:
              type: string
              example: "client@test.com"
            adresse_id:
              type: integer
              example: 3
    responses:
      201:
        description: Client créé
      400:
        description: Champs manquants
    """
    data = request.get_json() or {}

    email_client = data.get('email_client')
    adresse_id = data.get('adresse_id')

    if not email_client or not adresse_id:
        return jsonify({"error": "Champs manquants"}), 400

    client = repo.add(
        email_client=email_client,
        adresse_id=adresse_id
    )

    return jsonify({
        "message": "Client créé",
        "id": client.id
    }), 201


@colis_clients.route('/update/<int:client_id>', methods=['PUT'])
@login_required
@role_required('colis')
def update_client(client_id):
    """
    Met à jour un client
    ---
    tags:
      - Operateur Colis / Clients
    parameters:
      - name: client_id
        in: path
        required: true
        schema:
          type: integer
        description: ID du client
    requestBody:
      required: false
      content:
        application/json:
          schema:
            type: object
            properties:
              email_client:
                type: string
                example: "new@mail.com"
              adresse_id:
                type: integer
                example: 5
    responses:
      200:
        description: Client mis à jour
        content:
          application/json:
            example:
              message: "Client mis à jour"
              id: 1
      400:
        description: Aucun champ à mettre à jour
      404:
        description: Client non trouvé
    """
    data = request.get_json() or {}

    update_data = {}
    for field in ("email_client", "adresse_id"):
        if field in data:
            update_data[field] = data[field]

    if not update_data:
        return jsonify({"error": "Aucun champ à mettre à jour"}), 400

    client = repo.update(client_id, **update_data)
    if not client:
        return jsonify({"error": "Client non trouvé"}), 404

    return jsonify({
        "message": "Client mis à jour",
        "id": client_id
    }), 200



@colis_clients.route('/delete/<int:client_id>', methods=['DELETE'])
@login_required
@role_required('colis')
def delete_client(client_id):
    """
    Supprime un client
    ---
    tags:
      - Operateur Colis / Clients
    parameters:
      - name: client_id
        in: path
        required: true
        schema:
          type: integer
        description: ID du client à supprimer
    responses:
      200:
        description: Client supprimé
        content:
          application/json:
            example:
              message: "Client 1 supprimé"
      404:
        description: Client non trouvé
    """
    client = repo.get_by_id(client_id)
    if not client:
        return jsonify({"error": "Client non trouvé"}), 404

    repo.delete(client_id)
    return jsonify({
        "message": f"Client {client_id} supprimé"
    }), 200
