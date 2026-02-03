from digicheese.repositories.base_repository import BaseRepository
from ..models import Adresse


class AdresseRepository(BaseRepository):
    def __init__(self, session=None):
        super().__init__(Adresse, session)
