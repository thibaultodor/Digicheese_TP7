"""Repository for order detail operations."""
from digicheese.repositories.base_repository import BaseRepository
from ..models import DetailCommande


class DetailCommandeRepository(BaseRepository):
    """Repository for managing order details."""
    def __init__(self, session=None):
        super().__init__(DetailCommande, session)
