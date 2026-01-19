from digicheese.repositories.base_repository import BaseRepository
from ..models import Prix

class PrixRepository(BaseRepository):
    def __init__(self, session=None):
        super().__init__(Prix, session)