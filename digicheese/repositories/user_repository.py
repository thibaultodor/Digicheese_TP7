from typing import Optional
from sqlalchemy.orm import Session

from digicheese.models import Utilisateur
from ..models import Utilisateur as User, Utilisateur


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[type[Utilisateur]]:
        return self.session.query(Utilisateur).all()

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.session.get(User, user_id)

    def get_by_email(self, email: str) -> Optional[User]:
        return self.session.query(User).filter_by(email=email).first()

    def add(self, user: Utilisateur) -> Utilisateur:
        self.session.add(user)
        return user

    def commit(self) -> None:
        self.session.commit()
