from flasgger import swag_from
from flask import Blueprint, jsonify, request
from flask_login import login_required

operator = Blueprint('operator', __name__, url_prefix='/operator')

fake_orders = [
    {"id": 1, "item": "Potion", "quantity": 3},
    {"id": 2, "item": "Sword", "quantity": 1},
    {"id": 3, "item": "Shield", "quantity": 2}
]


@operator.route('/orders', methods=['GET'])
@login_required
@swag_from({
    'tags': ['Operator'],
    'responses': {
        200: {
            'description': 'Liste des commandes',
            'content': {
                'application/json': {
                    'example': fake_orders
                }
            }
        }
    }
})
def orders():
    return jsonify(fake_orders)


@operator.route('/order/<int:order_id>', methods=['GET'])
@login_required
@swag_from({
    'tags': ['Operator'],
    'parameters': [
        {
            'name': 'order_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID de la commande'
        }
    ],
    'responses': {
        200: {
            'description': 'Commande trouvée',
            'content': {
                'application/json': {
                    'example': {"id": 1, "item": "Potion", "quantity": 3}
                }
            }
        },
        404: {'description': 'Commande non trouvée'}
    }
})
def order(order_id):
    o = next((o for o in fake_orders if o["id"] == order_id), None)
    if o:
        return jsonify(o)
    return jsonify({"error": "Commande non trouvée"}), 404


@operator.route('/addOrder', methods=['POST'])
@login_required
@swag_from({
    'tags': ['Operator'],
    'responses': {
        201: {
            'description': 'Commande ajoutée',
            'content': {
                'application/json': {
                    'example': {"message": "Commande ajoutée", "order": {"id": 4, "item": "New Item", "quantity": 1}}
                }
            }
        }
    }
})
def addorder():
    new_order = {"id": len(fake_orders)+1, "item": "New Item", "quantity": 1}
    fake_orders.append(new_order)
    return jsonify({"message": "Commande ajoutée", "order": new_order}), 201


@operator.route('/updateOrder/<int:order_id>', methods=['PUT'])
@login_required
@swag_from({
    'tags': ['Operator'],
    'parameters': [
        {
            'name': 'order_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID de la commande à modifier'
        }
    ],
    'responses': {
        200: {
            'description': 'Commande modifiée',
            'content': {
                'application/json': {
                    'example': {"message": "Commande 1 modifiée", "order": {"id": 1, "item": "Potion", "quantity": 4}}
                }
            }
        },
        404: {'description': 'Commande non trouvée'}
    }
})
def updateorder(order_id):
    o = next((o for o in fake_orders if o["id"] == order_id), None)
    if o:
        o["quantity"] += 1
        return jsonify({"message": f"Commande {order_id} modifiée", "order": o})
    return jsonify({"error": "Commande non trouvée"}), 404


@operator.route('/deleteOrder/<int:order_id>', methods=['DELETE'])
@login_required
@swag_from({
    'tags': ['Operator'],
    'parameters': [
        {
            'name': 'order_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID de la commande à supprimer'
        }
    ],
    'responses': {
        200: {
            'description': 'Commande supprimée',
            'content': {
                'application/json': {
                    'example': {"message": "Commande 1 supprimée"}
                }
            }
        },
        404: {'description': 'Commande non trouvée'}
    }
})
def deleteorder(order_id):
    global fake_orders
    o = next((o for o in fake_orders if o["id"] == order_id), None)
    if o:
        fake_orders = [x for x in fake_orders if x["id"] != order_id]
        return jsonify({"message": f"Commande {order_id} supprimée"})
    return jsonify({"error": "Commande non trouvée"}), 404
