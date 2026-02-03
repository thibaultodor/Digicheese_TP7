from digicheese.repositories.base_repository import BaseRepository
from ..models import MiseAJour


class MiseAJourRepository(BaseRepository):
    def __init__(self, session=None):
        super().__init__(MiseAJour, session)
