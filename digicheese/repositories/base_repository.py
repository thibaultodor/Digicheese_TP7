"""Base repository class for database operations."""


class BaseRepository:
    """Base repository providing common CRUD operations."""

    model = None

    def __init__(self, model, session=None):
        self.model = model
        self.session = session

    def _commit(self):
        """Commit changes to the database with rollback on error."""
        try:
            self.session.commit()
        except Exception:
            self.session.rollback()
            raise

    def get_all(self):
        """Get all records of the model."""
        return self.session.query(self.model).all()

    def get_by_id(self, id_):
        """Get a record by its ID."""
        return self.session.get(self.model, id_)

    def add(self, obj=None, **kwargs):
        """Add a new record to the database."""
        if obj is None:
            obj = self.model(**kwargs)
        self.session.add(obj)
        self._commit()
        return obj

    def update(self, id_, **kwargs):
        """Update a record by its ID."""
        obj = self.get_by_id(id_)
        if obj is None:
            return None

        for key, value in kwargs.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        self._commit()
        return obj

    def delete(self, id_):
        """Delete a record by its ID."""
        obj = self.get_by_id(id_)
        if obj is None:
            return False

        self.session.delete(obj)
        self._commit()
        return True
