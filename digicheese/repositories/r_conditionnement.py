"""Repository for packaging operations."""
from digicheese.repositories.base_repository import BaseRepository
from ..models import Conditionnement


class ConditionnementRepository(BaseRepository):
    """Repository for managing packaging types."""
    def __init__(self, session=None):
        super().__init__(Conditionnement, session)
