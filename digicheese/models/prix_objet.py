"""Price model for managing object prices."""

from .. import db


class Prix(db.Model):
    """Price for one object (1:1 with Objet)."""

    __tablename__ = "prix"

    id = db.Column(db.Integer, primary_key=True)
    prix_objet = db.Column(db.Numeric(10, 2), nullable=False)
    objet_id = db.Column(
        db.Integer, db.ForeignKey("objet.id"), unique=True, nullable=False
    )

    objet = db.relationship("Objet", back_populates="prix")

    def to_json(self):
        """Convert price instance to JSON-serializable dictionary."""
        return {
            "id": self.id,
            "prix_objet": float(self.prix_objet),
            "objet_id": self.objet_id,
        }
