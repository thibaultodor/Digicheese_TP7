from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db

class Role(db.Model):
    """User role (admin / colis / stock)."""
    __tablename__ = "role"

    # Role id
    id = db.Column(db.Integer, primary_key=True)
    # Role name
    libelle = db.Column(db.String(50), unique=True, nullable=False)

    # Relations
    user_links = db.relationship("UserRole", back_populates="role", cascade="all, delete-orphan")

    # Methods
    def to_json(self):
        return {"id": self.id, "libelle": self.libelle}


class UserRole(db.Model):
    """Link table between User and Role (many-to-many).A user can have multiple roles."""
    __tablename__ = "roles_utilisateur"

    # FK to utilisateur.id
    user_id = db.Column(db.Integer, db.ForeignKey("utilisateur.id"), primary_key=True)
    # FK to role.id
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), primary_key=True)

    # Relations
    user = db.relationship("User", back_populates="role_links")
    role = db.relationship("Role", back_populates="user_links")


class User(db.Model, UserMixin):
    """Application user (utilisateur)."""
    __tablename__ = "utilisateur"

    # User id
    id = db.Column(db.Integer, primary_key=True)
    # Display name
    name = db.Column(db.String(100), nullable=False)
    # Unique email used to login
    email = db.Column(db.String(100), unique=True, nullable=False)
    # Hashed password
    password = db.Column(db.String(255), nullable=False)

    # Relations
    role_links = db.relationship("UserRole",back_populates="user",cascade="all, delete-orphan",lazy="joined",)

    # Methods
    def set_password(self, raw_password: str) -> None:
        """Hash and store the password."""
        self.password = generate_password_hash(raw_password, method="sha256")

    def check_password(self, raw_password: str) -> bool:
        """Check the password against the stored hash."""
        return check_password_hash(self.password, raw_password)

    def has_role(self, role_label: str) -> bool:
        """Return True if the user has the given role label."""
        return any(link.role.libelle == role_label for link in self.role_links)

    def to_json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "email": self.email,
            "roles": [link.role.libelle for link in self.role_links],
        }
