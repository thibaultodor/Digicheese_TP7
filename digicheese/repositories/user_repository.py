from typing import Optional
from sqlalchemy.orm import Session
from ..models import Utilisateur as User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.session.get(User, user_id)

    def get_by_email(self, email: str) -> Optional[User]:
        return self.session.query(User).filter_by(email=email).first()

    def add(self, user: User) -> User:
        self.session.add(user)
        return user

    def commit(self) -> None:
        self.session.commit()
