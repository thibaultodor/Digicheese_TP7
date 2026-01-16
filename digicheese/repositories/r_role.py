from ..models import Role

class RoleRepository:
    def __init__(self, session=None):
        self.session = session

    def _commit(self):
        try:
            self.session.commit()
        except Exception:
            self.session.rollback()
            raise

    def get_all(self):
        return self.session.query(Role).all()

    def get_by_id(self, id_):
        return self.session.get(Role, id_)

    def add(self, obj=None, **kwargs):
        if obj is None:
            obj = Role(**kwargs)
        self.session.add(obj)
        self._commit()
        return obj

    def update(self, id_, **kwargs):
        obj = self.get_by_id(id_)
        if obj is None:
            return None

        for key, value in kwargs.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        self._commit()
        return obj

    def delete(self, id_):
        obj = self.get_by_id(id_)
        if obj is None:
            return False

        self.session.delete(obj)
        self._commit()
        return True
