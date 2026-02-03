from .. import db


class Role(db.Model):
    """User role (admin / colis / stock)."""

    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(50), unique=True, nullable=False)

    user_links = db.relationship(
        "RolesUtilisateur", back_populates="role", cascade="all, delete-orphan"
    )

    def to_json(self):
        return {"id": self.id, "libelle": self.libelle}
