"""Repository for user roles operations."""
from digicheese.repositories.base_repository import BaseRepository
from ..models import RolesUtilisateur


class RolesUtilisateurRepository(BaseRepository):
    """Repository for managing user-role associations."""
    def __init__(self, session=None):
        super().__init__(RolesUtilisateur, session)
