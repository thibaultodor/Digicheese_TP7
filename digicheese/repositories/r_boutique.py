"""Repository for shop operations."""

from digicheese.repositories.base_repository import BaseRepository
from ..models import Boutique


class BoutiqueRepository(BaseRepository):
    """Repository for managing shops."""

    def __init__(self, session=None):
        super().__init__(Boutique, session)
