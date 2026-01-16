from .. import db

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