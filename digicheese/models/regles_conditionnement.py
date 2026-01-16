from .. import db

class RelCond(db.Model):
    """Packaging rule for an object (rel_cond)."""
    __tablename__ = "rel_cond"

    # Rule id
    id = db.Column(db.Integer, primary_key=True)
    # Quantity of object for this rule
    quantite_objet = db.Column(db.Integer, nullable=False)
    # FK to objet.id
    objet_id = db.Column(db.Integer, db.ForeignKey("objet.id"), nullable=False)
    # FK to conditionnement.id (packaging type)
    conditionnement_id = db.Column(db.Integer, db.ForeignKey("conditionnement.id"), nullable=True)

    # Relations
    objet = db.relationship("Objet", back_populates="rel_conds")
    conditionnement = db.relationship("Conditionnement", back_populates="rel_conds")

    # Methods
    def to_json(self):
        return {
            "id": self.id,
            "quantite_objet": self.quantite_objet,
            "objet_id": self.objet_id,
            "conditionnement_id": self.conditionnement_id,
        }