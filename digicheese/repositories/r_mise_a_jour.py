"""Repository for stock update operations."""
from digicheese.repositories.base_repository import BaseRepository
from ..models import MiseAJourStock


class MiseAJourRepository(BaseRepository):
    """Repository for managing stock updates."""
    def __init__(self, session=None):
        super().__init__(MiseAJour, session)
