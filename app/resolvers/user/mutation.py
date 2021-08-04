from fastapi import Depends

from graphene import Mutation, String, Boolean, Field, Int
from graphql import GraphQLError
from sqlalchemy.orm import Session

from app import database
from app import schemas

from app.models.user import User


class InsertUser(Mutation):
    class Arguments:
        username = String(required=True)
        email = String(required=True)
        password = String(required=True)

    user = Field(lambda: schemas.user.UserModel)

    def mutate(self, info, **kwargs):
        _ = self, info

        user: User = User()

        try:
            for key, value in kwargs.items():
                if key == 'password':
                    setattr(user, key, value + '_hashed')
                else:
                    setattr(user, key, value)
        except IndexError:
            return ""
        finally:
            db_session = database.esume.Session()

        try:
            db_session.add(user)
            db_session.commit()
        except Exception:
            raise GraphQLError('이미 등록된 계정입니다.')

        return InsertUser(user)


class UpdateUser(Mutation):
    class Arguments:
        id = Int()
        username = String()
        email = String()
        is_active = Boolean()

    ok = Boolean()
    user = Field(lambda: schemas.user.UserModel)

    def mutate(self, info, **kwargs):
        _ = self, info

        try:
            pk: int = kwargs.get('id')
        except KeyError:
            return ""
        finally:
            db_session = database.esume.Session()

        user: User = db_session.query(User).filter_by(id=pk).first()

        for key, value in kwargs.items():
            setattr(user, key, value)

        db_session.commit()

        return UpdateUser(user)


class DeleteUser(Mutation):
    class Arguments:
        id = Int()

    user = Field(lambda: schemas.user.UserModel)

    def mutate(self, info, **kwargs):
        _ = self, info

        try:
            pk: int = kwargs.get('id')
        except KeyError:
            return None
        finally:
            db_session = database.esume.Session()

        user: User = db_session.query(User).filter_by(id=pk).first()

        db_session.delete(user)
        db_session.commit()

        return DeleteUser(user)
