from digicheese.repositories.base_repository import BaseRepository
from ..models import Role


class RoleRepository(BaseRepository):
    def __init__(self, session=None):
        super().__init__(Role, session)
