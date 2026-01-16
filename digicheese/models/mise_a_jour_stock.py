from datetime import date
from .. import db

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