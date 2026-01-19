from digicheese.repositories.base_repository import BaseRepository
from ..models import Commune

class CommuneRepository(BaseRepository):
    def __init__(self, session=None):
        super().__init__(Commune, session)