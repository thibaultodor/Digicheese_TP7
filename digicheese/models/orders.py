from .. import db


class Conditionnement(db.Model):
    """Packaging / conditionnement."""
    __tablename__ = "conditionnement"

    # Conditionnement id
    id = db.Column(db.Integer, primary_key=True)
    # Packaging name
    libelle = db.Column(db.String(150), nullable=False)
    # Packaging weight
    poids_condit = db.Column(db.Numeric(10, 3), nullable=True)
    # Print order (if needed)
    ordre_imp = db.Column(db.Integer, nullable=True)

    # Relations
    commandes = db.relationship("Commande", back_populates="conditionnement")
    rel_conds = db.relationship("RelCond", back_populates="conditionnement")

    # Methods
    def to_json(self):
        return {
            "id": self.id,
            "libelle": self.libelle,
            "poids_condit": float(self.poids_condit) if self.poids_condit is not None else None,
            "ordre_imp": self.ordre_imp,
        }


class Commande(db.Model):
    """Order (commande) made by a client."""
    __tablename__ = "commande"

    # Commande id
    id = db.Column(db.Integer, primary_key=True)
    # Order date
    date = db.Column(db.Date, nullable=True)

    """
-----------------------------------------------------------------------------------------------------------------------
    J'avoue pas trop comprendre cette partie ? On parle plus de cheques ?
-----------------------------------------------------------------------------------------------------------------------
    """
    # Stamps paid by client (if used)
    timbre_client = db.Column(db.Integer, nullable=True)
    # Internal stamp code (if used)
    timbre_code = db.Column(db.String(50), nullable=True)

    # Number of packages
    nb_colis = db.Column(db.Integer, nullable=True)
    # Archived (command done) flag
    b_archive = db.Column(db.Boolean, default=False)
    # FK to client.id
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"), nullable=False)
    # FK to conditionnement.id
    conditionnement_id = db.Column(db.Integer, db.ForeignKey("conditionnement.id"), nullable=False)

    # Relations
    client = db.relationship("Client", back_populates="commandes")
    conditionnement = db.relationship("Conditionnement", back_populates="commandes")
    details = db.relationship("DetailCommande", back_populates="commande", cascade="all, delete-orphan")

    #Methods
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
