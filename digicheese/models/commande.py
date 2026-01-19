from .. import db

class Commande(db.Model):
    """Order (commande) made by a client."""
    __tablename__ = "commande"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=True)
    timbre_client = db.Column(db.Integer, nullable=True)
    timbre_code = db.Column(db.String(50), nullable=True)

    nb_colis = db.Column(db.Integer, nullable=True)
    b_archive = db.Column(db.Boolean, default=False)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"), nullable=False)
    conditionnement_id = db.Column(db.Integer, db.ForeignKey("conditionnement.id"), nullable=False)

    client = db.relationship("Client", back_populates="commandes")
    conditionnement = db.relationship("Conditionnement", back_populates="commandes")
    details = db.relationship("DetailCommande", back_populates="commande", cascade="all, delete-orphan")

    def to_json(self):
        return {
            "id": self.id,
            "date": self.date.isoformat() if self.date else None,
            "timbre_client": self.timbre_client,
            "timbre_code": self.timbre_code,
            "nb_colis": self.nb_colis,
            "b_archive": self.b_archive,
            "client_id": self.client_id,
            "conditionnement_id": self.conditionnement_id,
        }