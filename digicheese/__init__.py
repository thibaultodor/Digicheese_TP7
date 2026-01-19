from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flasgger import Swagger


# Initialize SQLAlchemy instance (outside create_app for import access)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # Configuration
    app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
    app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root@localhost:3306/digicheese?charset=utf8mb4' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions with app
    db.init_app(app)

    # Configure Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    # User loader function for Flask-Login
    from .models import Utilisateur as User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

    
    # Register blueprints
    from .routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from .routes.admin.user_route import admin_users as admin_users_blueprint
    app.register_blueprint(admin_users_blueprint)

    from .routes.admin.objet_route import admin_objets as admin_objets_blueprint
    app.register_blueprint(admin_objets_blueprint)

    from .routes.admin.commune_route import admin_communes as admin_communes_blueprint
    app.register_blueprint(admin_communes_blueprint)

    # from .routes.operatorRouter import operator as operator_blueprint
    # app.register_blueprint(operator_blueprint)

    Swagger(app)

    with app.app_context():
        db.create_all()

    return app