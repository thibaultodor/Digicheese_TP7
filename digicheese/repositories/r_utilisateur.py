"""Repository for user operations."""
from digicheese.repositories.base_repository import BaseRepository
from ..models import Utilisateur


class UtilisateurRepository(BaseRepository):
    """Repository for managing users."""
    def __init__(self, session=None):
        super().__init__(Utilisateur, session)
