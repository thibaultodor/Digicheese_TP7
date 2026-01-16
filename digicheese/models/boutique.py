from .. import db

"""
Boutique: separate dated quantity tracking for an object in boutique context.
"""

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