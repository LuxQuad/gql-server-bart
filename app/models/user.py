from app.database import esume

from sqlalchemy import Boolean, Column, String, Integer


class User(esume.Base):
    __tablename__: str = "users"

    # Identifier
    id: int = Column(Integer, primary_key=True, index=True)

    # Column
    email: str = Column(String, unique=True, index=True)
    username: str = Column(String, unique=True, index=True)
    password: str = Column(String)

    is_active: bool = Column(Boolean, default=True)
