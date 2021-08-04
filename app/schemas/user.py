from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from app.models import user


class UserModel(SQLAlchemyObjectType):
    class Meta:
        model = user.User
        interfaces = (relay.Node,)


class UserConnection(relay.Connection):
    class Meta:
        node = UserModel
