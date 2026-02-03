from .. import db


class RolesUtilisateur(db.Model):
    """Link table between User and Role (many-to-many).A user can have multiple roles."""

    __tablename__ = "roles_utilisateur"

    user_id = db.Column(db.Integer, db.ForeignKey("utilisateur.id"), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), primary_key=True)

    user = db.relationship("Utilisateur", back_populates="role_links")
    role = db.relationship("Role", back_populates="user_links")
