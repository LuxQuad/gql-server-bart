from graphene import String, Mutation, Boolean, Int, Field

from app import dependencies
from app import schemas
from app import models


class InsertUser(Mutation):
    class Arguments:
        username: str = String(required=True)
        email: str = String(required=True)
        password: str = String(required=True)

    user = Field(lambda: schemas.user.UserModel)

    @staticmethod
    def mutate(info, **kwargs):
        _ = info

        user = models.user.User

        try:
            for key, value in kwargs.items():
                if key == 'password':
                    setattr(user, 'hashed_password', value + '_hashed')
                else:
                    setattr(user, user.key, value)
        except IndexError:
            return ""
        finally:
            database = dependencies.get_db()

        database.esume.SessionLocal.add(user)
        database.esume.SessionLocal.commit()

        return user


class UpdateUser(Mutation):
    class Arguments:
        id: int = Int()
        username: str = String()
        email: str = String()
        is_active: bool = Boolean()

    user = Field(lambda: schemas.user.UserModel)

    @staticmethod
    def mutate(info, **kwargs):
        _ = info

        try:
            pk = kwargs.get('id')
        except KeyError:
            return ""
        finally:
            database = dependencies.get_db()

        user = database.esume.SessionLocal.query(models.user.User).filter_by(id=pk).first()

        for key, value in kwargs.items():
            setattr(user, user.key, value)

        database.esume.SessionLocal.commit()

        return user


class DeleteUser(Mutation):
    class Arguments:
        id: int = Int()

    user = Field(lambda: schemas.user.UserModel)

    @staticmethod
    def mutate(info, **kwargs):
        _ = info

        try:
            pk = kwargs.get('id')
        except KeyError:
            return None
        finally:
            database = dependencies.get_db()

        user = database.esume.SessionLocal.query(models.user.User).filter_by(id=pk).first()
        database.esume.SessionLocal.delete(user)

        return ""
