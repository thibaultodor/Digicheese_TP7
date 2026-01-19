from .. import db

class Objet(db.Model):
    """Gift item / goodie (objet)."""
    __tablename__ = "objet"

    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(150), nullable=False)
    taille = db.Column(db.String(50), nullable=True)
    poids = db.Column(db.Numeric(10, 3), nullable=True)
    bl_indispo = db.Column(db.Boolean, default=False)

    prix = db.relationship("Prix", back_populates="objet", uselist=False, cascade="all, delete-orphan")
    mises_a_jour = db.relationship("MiseAJour", back_populates="objet", cascade="all, delete-orphan")
    detail_commandes = db.relationship("DetailCommande", back_populates="objet")
    stock_lignes = db.relationship("StockLigne", back_populates="objet")
    boutiques = db.relationship("Boutique", back_populates="objet")
    rel_conds = db.relationship("RelCond", back_populates="objet")

    def to_json(self):
        return {
            "id": self.id,
            "libelle": self.libelle,
            "taille": self.taille,
            "poids": float(self.poids) if self.poids is not None else None,
            "bl_indispo": self.bl_indispo,
        }