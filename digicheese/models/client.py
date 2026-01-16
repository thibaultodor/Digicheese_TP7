from .. import db

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