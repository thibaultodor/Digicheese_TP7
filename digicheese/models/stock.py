from .. import db

"""
Stock: list of stock locations/types.
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