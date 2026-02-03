"""Repository for object/product operations."""
from digicheese.repositories.base_repository import BaseRepository
from ..models import Objet


class ObjetRepository(BaseRepository):
    """Repository for managing objects/products."""
    def __init__(self, session=None):
        super().__init__(Objet, session)
