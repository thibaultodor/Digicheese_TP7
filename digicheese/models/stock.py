from .. import db

"""
Stock: list of stock locations/types.
"""

class Stock(db.Model):
    """Stock entity (stock)."""
    __tablename__ = "stock"

    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(150), nullable=False)

    lignes = db.relationship("StockLigne", back_populates="stock")

    def to_json(self):
        return {"id": self.id, "libelle": self.libelle}