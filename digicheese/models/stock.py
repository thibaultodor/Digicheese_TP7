"""Stock model for managing stock locations and types."""
from .. import db


class Stock(db.Model):
    """Stock entity (stock)."""

    __tablename__ = "stock"

    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(150), nullable=False)

    lignes = db.relationship("StockLigne", back_populates="stock")

    def to_json(self):
        """Convert stock instance to JSON-serializable dictionary."""
        return {"id": self.id, "libelle": self.libelle}
