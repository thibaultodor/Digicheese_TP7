from .. import db

class Conditionnement(db.Model):
    """Packaging / conditionnement."""
    __tablename__ = "conditionnement"

    # Conditionnement id
    id = db.Column(db.Integer, primary_key=True)
    # Packaging name
    libelle = db.Column(db.String(150), nullable=False)
    # Packaging weight
    poids_condit = db.Column(db.Numeric(10, 3), nullable=True)
    # Print order (if needed)
    ordre_imp = db.Column(db.Integer, nullable=True)

    # Relations
    commandes = db.relationship("Commande", back_populates="conditionnement")
    rel_conds = db.relationship("RelCond", back_populates="conditionnement")

    # Methods
    def to_json(self):
        return {
            "id": self.id,
            "libelle": self.libelle,
            "poids_condit": float(self.poids_condit) if self.poids_condit is not None else None,
            "ordre_imp": self.ordre_imp,
        }