from app.database import esume

from sqlalchemy import Boolean, Column, String, Integer


class User(esume.Base):
    __tablename__: str = "users"

    # Identifier
    id = Column(Integer, primary_key=True, index=True)

    # Column
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    is_active = Column(Boolean, default=True)
