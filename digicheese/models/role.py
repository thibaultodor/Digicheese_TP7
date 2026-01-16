from .. import db

class Role(db.Model):
    """User role (admin / colis / stock)."""
    __tablename__ = "role"

    # Role id
    id = db.Column(db.Integer, primary_key=True)
    # Role name
    libelle = db.Column(db.String(50), unique=True, nullable=False)

    # Relations
    user_links = db.relationship("RolesUtilisateur", back_populates="role", cascade="all, delete-orphan")

    # Methods
    def to_json(self):
        return {"id": self.id, "libelle": self.libelle}