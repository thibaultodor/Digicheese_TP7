"""Repository for order operations."""
from digicheese.repositories.base_repository import BaseRepository
from ..models import Commande


class CommandeRepository(BaseRepository):
    """Repository for managing orders."""
    def __init__(self, session=None):
        super().__init__(Commande, session)
