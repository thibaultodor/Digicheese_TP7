from digicheese.repositories.base_repository import BaseRepository
from ..models import Boutique

class BoutiqueRepository(BaseRepository):
    def __init__(self, session=None):
        super().__init__(Boutique, session)