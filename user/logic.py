from dataclasses import dataclass

from sqlalchemy import insert, select
from sqlalchemy.orm import Session

from user.models import UserProfile
from user.schemas import UserCreateSchema


@dataclass
class UserLogic:
    db_session: Session

    def get_google_user_by_email(self, email: str) -> UserProfile | None:
        query = select(UserProfile).where(UserProfile.email == email)
        with self.db_session as session:
            return session.execute(query).scalar_one_or_none()

    def create_user(self, user: UserCreateSchema) -> UserProfile:
        query = insert(UserProfile).values(**user.model_dump()).returning(UserProfile.id)

        with self.db_session as session:
            user_id: int = session.execute(query).scalar()
            session.commit()
            session.flush()
            return self.get_user(user_id)

    def get_user(self, user_id: int) -> UserProfile | None:
        with self.db_session as session:
            return session.query(UserProfile).filter(UserProfile.id == user_id).one_or_none()

    def get_user_by_username(self, username: str) -> UserProfile | None:
        query = select(UserProfile).where(UserProfile.username == username)
        with self.db_session as session:
            user: UserProfile = session.execute(query).scalar_one_or_none()
            return user
