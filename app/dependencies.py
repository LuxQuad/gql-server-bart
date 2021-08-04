"""
@Author:
    Bart Kim 

@Note:

"""
from app import database


async def get_db():
    db = database.esume.SessionLocal()

    try:
        yield db
    finally:
        db.close()
