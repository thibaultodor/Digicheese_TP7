from .. import db

class Adresse(db.Model):
    """Address (3 address lines) linked to one commune."""
    __tablename__ = "adresse"

    # id of the address
    id = db.Column(db.Integer, primary_key=True)
    # Address lines
    comp_adresse1 = db.Column(db.String(255), nullable=False)
    comp_adresse2 = db.Column(db.String(255), nullable=True)
    comp_adresse3 = db.Column(db.String(255), nullable=True)
    # FK to commune.cp
    commune_cp = db.Column(db.String(10), db.ForeignKey("commune.cp"), nullable=False)

    # Relations
    commune = db.relationship("Commune", back_populates="adresses")
    clients = db.relationship("Client", back_populates="adresse")

    # Methods
    def to_json(self):
        return {
            "id": self.id,
            "comp_adresse1": self.comp_adresse1,
            "comp_adresse2": self.comp_adresse2,
            "comp_adresse3": self.comp_adresse3,
            "commune_cp": self.commune_cp,
        }