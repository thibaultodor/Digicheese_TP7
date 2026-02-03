from flask import Blueprint, jsonify
from flask_login import login_required

from digicheese.decorator.role_required import role_required

colis_statistique = Blueprint(
    "colis_statistique", __name__, url_prefix="/colis/statistique"
)


@colis_statistique.route("/statistique", methods=["GET"])
@login_required
@role_required("colis")
def get_statistiques():
    """
    Récupère un exemple de statistiques de colis
    ---
    tags:
      - Operateur Colis / Statistiques
    responses:
      200:
        description: Exemple de statistiques
        content:
          application/json:
            example:
              total_colis: 120
              colis_livres: 85
              colis_en_attente: 35
              pourcentage_livres: 70.8
    """
    stats_example = {
        "total_colis": 120,
        "colis_livres": 85,
        "colis_en_attente": 35,
        "pourcentage_livres": 70.8,
    }

    return jsonify(stats_example), 200
