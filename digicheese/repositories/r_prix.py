"""Repository for price operations."""
from digicheese.repositories.base_repository import BaseRepository
from ..models import PrixObjet


class PrixRepository(BaseRepository):
    """Repository for managing object prices."""
    def __init__(self, session=None):
        super().__init__(Prix, session)
