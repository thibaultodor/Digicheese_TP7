from .. import db


class Client(db.Model):
    """Client (customer) linked to one address."""

    __tablename__ = "client"

    id = db.Column(db.Integer, primary_key=True)
    email_client = db.Column(db.String(150), nullable=True)
    adresse_id = db.Column(db.Integer, db.ForeignKey("adresse.id"), nullable=False)

    adresse = db.relationship("Adresse", back_populates="clients")
    commandes = db.relationship("Commande", back_populates="client")

    def to_json(self):
        return {
            "id": self.id,
            "email_client": self.email_client,
            "adresse_id": self.adresse_id,
        }
