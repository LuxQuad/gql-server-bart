from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from app.settings import settings

Engine = create_engine(
    settings.ESUME_DATABASE_URL,
    connect_args={}
)

SessionMarker = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
Session = SessionMarker

Base = declarative_base()
Base.query = scoped_session(Session).query_property()
