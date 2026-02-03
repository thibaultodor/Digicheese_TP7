from flask import Blueprint, jsonify
from flask_login import login_required

from digicheese.decorator.role_required import role_required

colis_mailler = Blueprint("colis_mailler", __name__, url_prefix="/colis/mailler")


@colis_mailler.route("/template", methods=["GET"])
@login_required
@role_required("colis")
def get_mail_template():
    """
    Récupère un exemple de template de mail
    ---
    tags:
      - Operateur Colis / Mailer
    responses:
      200:
        description: Template de mail exemple
        content:
          application/json:
            example:
              subject: "Votre colis est prêt à l'expédition"
              body: |
                Bonjour {{ client_name }},

                Votre colis n°{{ commande_id }} est prêt à être expédié.

                Adresse de livraison :
                {{ adresse }}

                Merci de votre confiance.
    """
    template = {
        "subject": "Votre colis est prêt à l'expédition",
        "body": (
            "Bonjour {{ client_name }},\n\n"
            "Votre colis n°{{ commande_id }} est prêt à être expédié.\n\n"
            "Adresse de livraison :\n"
            "{{ adresse }}\n\n"
            "Merci de votre confiance."
        ),
    }

    return jsonify(template), 200
