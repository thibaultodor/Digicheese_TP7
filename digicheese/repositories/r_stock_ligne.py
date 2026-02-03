"""Repository for stock line operations."""

from digicheese.repositories.base_repository import BaseRepository
from ..models import StockLigne


class StockLigneRepository(BaseRepository):
    """Repository for managing stock lines."""

    def __init__(self, session=None):
        super().__init__(StockLigne, session)
