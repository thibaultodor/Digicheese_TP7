from digicheese.repositories.base_repository import BaseRepository
from ..models import Stock

class StockRepository(BaseRepository):
    def __init__(self, session=None):
        super().__init__(Stock, session)