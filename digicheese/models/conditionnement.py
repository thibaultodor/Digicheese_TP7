"""Packaging model for managing packaging types."""
from .. import db


class Conditionnement(db.Model):
    """Packaging / conditionnement."""

    __tablename__ = "conditionnement"

    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(150), nullable=False)
    poids_condit = db.Column(db.Numeric(10, 3), nullable=True)
    ordre_imp = db.Column(db.Integer, nullable=True)

    commandes = db.relationship("Commande", back_populates="conditionnement")
    rel_conds = db.relationship("RelCond", back_populates="conditionnement")

    def to_json(self):
        """Convert packaging instance to JSON-serializable dictionary."""
        return {
            "id": self.id,
            "libelle": self.libelle,
            "poids_condit": (
                float(self.poids_condit) if self.poids_condit is not None else None
            ),
            "ordre_imp": self.ordre_imp,
        }
