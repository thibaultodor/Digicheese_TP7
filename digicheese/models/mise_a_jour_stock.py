"""Stock update model for tracking inventory changes."""
from datetime import date
from .. import db


class MiseAJour(db.Model):
    """Stock update (mise_a_jour) linked to an object."""

    __tablename__ = "mise_a_jour"

    id = db.Column(db.Integer, primary_key=True)
    quantite_maj = db.Column(db.Integer, nullable=False)
    date_maj = db.Column(db.Date, nullable=False, default=date.today)
    objet_id = db.Column(db.Integer, db.ForeignKey("objet.id"), nullable=False)

    objet = db.relationship("Objet", back_populates="mises_a_jour")

    def to_json(self):
        """Convert stock update instance to JSON-serializable dictionary."""
        return {
            "id": self.id,
            "quantite_maj": self.quantite_maj,
            "date_maj": self.date_maj.isoformat(),
            "objet_id": self.objet_id,
        }
