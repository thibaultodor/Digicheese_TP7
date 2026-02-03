"""Packaging rules model for managing object packaging configurations."""

from .. import db


class RelCond(db.Model):
    """Packaging rule for an object (rel_cond)."""

    __tablename__ = "rel_cond"

    id = db.Column(db.Integer, primary_key=True)
    quantite_objet = db.Column(db.Integer, nullable=False)
    objet_id = db.Column(db.Integer, db.ForeignKey("objet.id"), nullable=False)
    conditionnement_id = db.Column(
        db.Integer, db.ForeignKey("conditionnement.id"), nullable=True
    )

    objet = db.relationship("Objet", back_populates="rel_conds")
    conditionnement = db.relationship(
        "Conditionnement", back_populates="rel_conds"
    )

    def to_json(self):
        """Convert packaging rule instance to JSON-serializable dictionary."""
        return {
            "id": self.id,
            "quantite_objet": self.quantite_objet,
            "objet_id": self.objet_id,
            "conditionnement_id": self.conditionnement_id,
        }
