"""
@Author:
    Bart Kim 

@Note:

"""
from app import database


def get_db():
    db = database.esume.Session()

    try:
        yield db
    finally:
        db.close()
