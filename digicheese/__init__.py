"""
Digicheese application package.

This module initializes the Flask application and configures extensions.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flasgger import Swagger

# Initialize SQLAlchemy instance (outside create_app for import access)
db = SQLAlchemy()


def create_app():
    """
    Create and configure the Flask application.

    Returns:
        Flask: Configured Flask application instance.
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "your-secret-key-change-in-production"
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mysql+pymysql://root@localhost:3306/digicheese?charset=utf8mb4"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions with app
    db.init_app(app)

    # Configure Flask-Login
    login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Register blueprints
    from .models import Utilisateur as User
    from .routes.auth import auth as auth_blueprint
    from .routes.main import main as main_blueprint
    from .routes.admin.user_route import admin_users as admin_users_blueprint
    from .routes.admin.objet_route import (
        admin_objets as admin_objets_blueprint,
    )
    from .routes.admin.commune_route import (
        admin_communes as admin_communes_blueprint,
    )

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(admin_users_blueprint)
    app.register_blueprint(admin_objets_blueprint)
    app.register_blueprint(admin_communes_blueprint)

    # User loader function for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes.admin.conditionnemens_route import (
        admin_conditionnements as admin_conditionnements_blueprint,
    )

    app.register_blueprint(admin_conditionnements_blueprint)

    from .routes.colis.client_route import (
        colis_clients as colis_clients_blueprint,
    )

    app.register_blueprint(colis_clients_blueprint)

    from .routes.colis.adresse_route import (
        colis_adresses as colis_adresses_blueprint,
    )

    app.register_blueprint(colis_adresses_blueprint)

    from .routes.colis.commande_route import (
        colis_commandes as colis_commandes_blueprint,
    )

    app.register_blueprint(colis_commandes_blueprint)

    from .routes.colis.detail_commande_route import (
        colis_detail_commandes as colis_detail_commandes_blueprint,
    )

    app.register_blueprint(colis_detail_commandes_blueprint)

    from .routes.colis.mailler_route import (
        colis_mailler as colis_mailler_blueprint,
    )

    app.register_blueprint(colis_mailler_blueprint)

    from .routes.colis.statistique_route import (
        colis_statistique as colis_statistiques_blueprint,
    )

    app.register_blueprint(colis_statistiques_blueprint)

    Swagger(app)

    with app.app_context():
        db.create_all()

    return app
