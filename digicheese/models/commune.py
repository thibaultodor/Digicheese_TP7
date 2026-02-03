from .. import db


class Commune(db.Model):
    """Commune referential (postal code, city, department)."""

    __tablename__ = "commune"

    cp = db.Column(db.String(10), primary_key=True)
    commune = db.Column(db.String(120), nullable=False)
    departement = db.Column(db.String(120), nullable=True)

    adresses = db.relationship("Adresse", back_populates="commune")

    def to_json(self):
        return {
            "cp": self.cp,
            "commune": self.commune,
            "departement": self.departement,
        }
