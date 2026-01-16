from .. import db

class Commune(db.Model):
    """Commune referential (postal code, city, department)."""
    __tablename__ = "commune"
    # Postal code (id for city)
    cp = db.Column(db.String(10), primary_key=True)
    # City name
    commune = db.Column(db.String(120), nullable=False)
    # Department name/number
    departement = db.Column(db.String(120), nullable=True)

    # Relations
    adresses = db.relationship("Adresse", back_populates="commune")

    # Methods
    def to_json(self):
        return {
            "cp": self.cp,
            "commune": self.commune,
            "departement": self.departement,
        }