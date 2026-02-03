"""Order detail model for managing items in orders."""

from .. import db


class DetailCommande(db.Model):
    """Order detail (detail_commande)."""

    __tablename__ = "detail_commande"

    id = db.Column(db.Integer, primary_key=True)
    quantite = db.Column(db.Integer, nullable=False, default=1)
    colis = db.Column(db.Integer, nullable=True)
    commentaire = db.Column(db.Text, nullable=True)
    commande_id = db.Column(
        db.Integer, db.ForeignKey("commande.id"), nullable=False
    )
    objet_id = db.Column(db.Integer, db.ForeignKey("objet.id"), nullable=False)

    commande = db.relationship("Commande", back_populates="details")
    objet = db.relationship("Objet", back_populates="detail_commandes")

    def to_json(self):
        """Convert order detail instance to JSON-serializable dictionary."""
        return {
            "id": self.id,
            "quantite": self.quantite,
            "colis": self.colis,
            "commentaire": self.commentaire,
            "commande_id": self.commande_id,
            "objet_id": self.objet_id,
        }
