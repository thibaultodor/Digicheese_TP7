from datetime import date
from .. import db


class Objet(db.Model):
    """Gift item / goodie (objet)."""
    __tablename__ = "objet"

    # Object id
    id = db.Column(db.Integer, primary_key=True)
    # Item name
    libelle = db.Column(db.String(150), nullable=False)
    # Size (optional)
    taille = db.Column(db.String(50), nullable=True)
    # Item weight
    poids = db.Column(db.Numeric(10, 3), nullable=True)

    # True if item is unavailable
    bl_indispo = db.Column(db.Boolean, default=False)

    # Relations
    prix = db.relationship("Prix", back_populates="objet", uselist=False, cascade="all, delete-orphan")
    mises_a_jour = db.relationship("MiseAJour", back_populates="objet", cascade="all, delete-orphan")
    detail_commandes = db.relationship("DetailCommande", back_populates="objet")
    stock_lignes = db.relationship("StockLigne", back_populates="objet")
    boutiques = db.relationship("Boutique", back_populates="objet")
    rel_conds = db.relationship("RelCond", back_populates="objet")

    # Methods
    def to_json(self):
        return {
            "id": self.id,
            "libelle": self.libelle,
            "taille": self.taille,
            "poids": float(self.poids) if self.poids is not None else None,
            "bl_indispo": self.bl_indispo,
        }


class Prix(db.Model):
    """Price for one object (1:1 with Objet)."""
    __tablename__ = "prix"

    # Price id
    id = db.Column(db.Integer, primary_key=True)
    # Object price
    prix_objet = db.Column(db.Numeric(10, 2), nullable=False)
    # FK to objet.id (unique => 1:1)
    objet_id = db.Column(db.Integer, db.ForeignKey("objet.id"), unique=True, nullable=False)

    # Relations
    objet = db.relationship("Objet", back_populates="prix")

    # Methods
    def to_json(self):
        return {
            "id": self.id,
            "prix_objet": float(self.prix_objet),
            "objet_id": self.objet_id,
        }


class MiseAJour(db.Model):
    """Stock update (mise_a_jour) linked to an object."""
    __tablename__ = "mise_a_jour"

    # Update id
    id = db.Column(db.Integer, primary_key=True)
    # Quantity updated
    quantite_maj = db.Column(db.Integer, nullable=False)
    # Update date
    date_maj = db.Column(db.Date, nullable=False, default=date.today)
    # FK to objet.id
    objet_id = db.Column(db.Integer, db.ForeignKey("objet.id"), nullable=False)

    # Relations
    objet = db.relationship("Objet", back_populates="mises_a_jour")

    # Methods
    def to_json(self):
        return {
            "id": self.id,
            "quantite_maj": self.quantite_maj,
            "date_maj": self.date_maj.isoformat(),
            "objet_id": self.objet_id,
        }


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