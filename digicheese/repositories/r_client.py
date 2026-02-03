"""Repository for client operations."""

from digicheese.repositories.base_repository import BaseRepository
from ..models import Client


class ClientRepository(BaseRepository):
    """Repository for managing clients."""

    def __init__(self, session=None):
        super().__init__(Client, session)
