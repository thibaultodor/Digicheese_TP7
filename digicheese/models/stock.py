from .. import db

"""
Stock: list of stock locations/types.
StockLigne: stock quantities for an object (optionally linked to a stock), with optional dates for history.
Boutique: separate dated quantity tracking for an object in boutique context.
"""

class Stock(db.Model):
    """Stock entity (stock)."""
    __tablename__ = "stock"

    # Stock id
    id = db.Column(db.Integer, primary_key=True)
    # Type de Stock
    libelle = db.Column(db.String(150), nullable=False)

    # Relations
    lignes = db.relationship("StockLigne", back_populates="stock")

    # Methods
    def to_json(self):
        return {"id": self.id, "libelle": self.libelle}


class StockLigne(db.Model):
    """Stock line (stock_ligne) linked to an object and (optionally) a stock."""
    __tablename__ = "stock_ligne"

    # History id
    id = db.Column(db.Integer, primary_key=True)
    # Label (Free text)
    libelle = db.Column(db.String(150), nullable=False)
    # Start date (history)
    date_deb = db.Column(db.Date, nullable=True)
    # End date (history)
    date_fin = db.Column(db.Date, nullable=True)
    # Quantity
    quantite_stock = db.Column(db.Integer, nullable=False, default=0)
    # FK to objet.id
    objet_id = db.Column(db.Integer, db.ForeignKey("objet.id"), nullable=False)
    # FK to stock.id
    # stock_id can be null if the line is not attached to a specific stock
    stock_id = db.Column(db.Integer, db.ForeignKey("stock.id"), nullable=True)

    # Relations
    objet = db.relationship("Objet", back_populates="stock_lignes")
    stock = db.relationship("Stock", back_populates="lignes")

    # Methods
    def to_json(self):
        return {
            "id": self.id,
            "libelle": self.libelle,
            "date_deb": self.date_deb.isoformat() if self.date_deb else None,
            "date_fin": self.date_fin.isoformat() if self.date_fin else None,
            "quantite_stock": self.quantite_stock,
            "objet_id": self.objet_id,
            "stock_id": self.stock_id,
        }


class Boutique(db.Model):
    """Boutique tracking linked to an object."""
    __tablename__ = "boutique"

    # Boutique id
    id = db.Column(db.Integer, primary_key=True)
    # Record date
    date = db.Column(db.Date, nullable=True)
    # Quantity for boutique
    quantite_boutique = db.Column(db.Integer, nullable=False, default=0)
    # FK to objet.id
    objet_id = db.Column(db.Integer, db.ForeignKey("objet.id"), nullable=False)

    # Relations
    objet = db.relationship("Objet", back_populates="boutiques")

    # Methods
    def to_json(self):
        return {
            "id": self.id,
            "date": self.date.isoformat() if self.date else None,
            "quantite_boutique": self.quantite_boutique,
            "objet_id": self.objet_id,
        }