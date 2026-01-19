from digicheese.repositories.base_repository import BaseRepository
from ..models import Conditionnement

class ConditionnementRepository(BaseRepository):
    def __init__(self, session=None):
        super().__init__(Conditionnement, session)