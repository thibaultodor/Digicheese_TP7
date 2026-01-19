from .. import db

"""
StockLigne: stock quantities for an object (optionally linked to a stock), with optional dates for history.
"""

class StockLigne(db.Model):
    """Stock line (stock_ligne) linked to an object and (optionally) a stock."""
    __tablename__ = "stock_ligne"

    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(150), nullable=False)
    date_deb = db.Column(db.Date, nullable=True)
    date_fin = db.Column(db.Date, nullable=True)
    quantite_stock = db.Column(db.Integer, nullable=False, default=0)
    objet_id = db.Column(db.Integer, db.ForeignKey("objet.id"), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey("stock.id"), nullable=True)

    objet = db.relationship("Objet", back_populates="stock_lignes")
    stock = db.relationship("Stock", back_populates="lignes")

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