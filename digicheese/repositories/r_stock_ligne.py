from digicheese.repositories.base_repository import BaseRepository
from ..models import StockLigne


class StockLigneRepository(BaseRepository):
    def __init__(self, session=None):
        super().__init__(StockLigne, session)
