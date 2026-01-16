# Repositories (CRUD helpers)
from .r_utilisateur import UtilisateurRepository
from .r_role import RoleRepository
from .r_roles_utilisateur import RolesUtilisateurRepository
from .r_objet import ObjetRepository
from .r_prix import PrixRepository
from .r_mise_a_jour import MiseAJourRepository
from .r_rel_cond import RelCondRepository
from .r_commune import CommuneRepository
from .r_adresse import AdresseRepository
from .r_client import ClientRepository
from .r_conditionnement import ConditionnementRepository
from .r_commande import CommandeRepository
from .r_detail_commande import DetailCommandeRepository
from .r_stock import StockRepository
from .r_stock_ligne import StockLigneRepository
from .r_boutique import BoutiqueRepository

__all__ = [
    "UtilisateurRepository",
    "RoleRepository",
    "RolesUtilisateurRepository",
    "ObjetRepository",
    "PrixRepository",
    "MiseAJourRepository",
    "RelCondRepository",
    "CommuneRepository",
    "AdresseRepository",
    "ClientRepository",
    "ConditionnementRepository",
    "CommandeRepository",
    "DetailCommandeRepository",
    "StockRepository",
    "StockLigneRepository",
    "BoutiqueRepository",
]
