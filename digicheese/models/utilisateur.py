"""User model for application authentication and authorization."""
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db


class Utilisateur(db.Model, UserMixin):
    """Application user (utilisateur)."""

    __tablename__ = "utilisateur"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    role_links = db.relationship(
        "RolesUtilisateur",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="joined",
    )

    def set_password(self, raw_password: str) -> None:
        """Hash and store the password."""
        self.password = generate_password_hash(raw_password)

    def check_password(self, raw_password: str) -> bool:
        """Check the password against the stored hash."""
        return check_password_hash(self.password, raw_password)

    def has_role(self, role_label: str) -> bool:
        """Return True if the user has the given role label."""
        return any(link.role.libelle == role_label for link in self.role_links)

    def __str__(self):
        return f"Utilisateur(id={self.id}, name={self.name}, email={self.email})"

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "roles": [link.role.libelle for link in self.role_links],
        }
