from digicheese.repositories.base_repository import BaseRepository
from ..models import RelCond


class RelCondRepository(BaseRepository):
    def __init__(self, session=None):
        super().__init__(RelCond, session)
