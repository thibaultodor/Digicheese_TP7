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


class Client(db.Model):
    """Client (customer) linked to one address."""
    __tablename__ = "client"

    # Customer id
    id = db.Column(db.Integer, primary_key=True)
    # Customer email (optional)
    email_client = db.Column(db.String(150), nullable=True)
    # FK to adresse.id
    adresse_id = db.Column(db.Integer, db.ForeignKey("adresse.id"), nullable=False)

    # Relations
    adresse = db.relationship("Adresse", back_populates="clients")
    commandes = db.relationship("Commande", back_populates="client")

    # Methods
    def to_json(self):
        return {
            "id": self.id,
            "email_client": self.email_client,
            "adresse_id": self.adresse_id,
        }
