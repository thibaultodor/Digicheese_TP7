from .. import db

class DetailCommande(db.Model):
    """Order detail (detail_commande)."""
    __tablename__ = "detail_commande"

    # Order details id
    id = db.Column(db.Integer, primary_key=True)
    # Quantity of the object
    quantite = db.Column(db.Integer, nullable=False, default=1)
    # Package(s) number(s)
    colis = db.Column(db.Integer, nullable=True)
    # Free comment
    commentaire = db.Column(db.Text, nullable=True)
    # FK to commande.id
    commande_id = db.Column(db.Integer, db.ForeignKey("commande.id"), nullable=False)
    # FK to objet.id
    objet_id = db.Column(db.Integer, db.ForeignKey("objet.id"), nullable=False)

    # Relations
    commande = db.relationship("Commande", back_populates="details")
    objet = db.relationship("Objet", back_populates="detail_commandes")

    #Methods
    def to_json(self):
        return {
            "id": self.id,
            "quantite": self.quantite,
            "colis": self.colis,
            "commentaire": self.commentaire,
            "commande_id": self.commande_id,
            "objet_id": self.objet_id,
        }
