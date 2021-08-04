from typing import Optional, Any

from graphene import ObjectType, relay, Int
from graphene_sqlalchemy import SQLAlchemyConnectionField

from app import schemas
from . import mutation


class Query(ObjectType):
    node = relay.Node.Field()

    user = SQLAlchemyConnectionField(schemas.user.UserConnection, id=Int())
    user_list = SQLAlchemyConnectionField(schemas.user.UserConnection, sort=schemas.user.UserModel.sort_argument())

    def resolve_user(self, info, **kwarg) -> Optional[Any]:
        _ = self

        try:
            pk: int = kwarg.get('id')
        except KeyError:
            return None

        users_query = schemas.user.UserModel.get_query(info)

        if pk is not None:
            return users_query.filter_by(id=pk)


class Mutation(ObjectType):
    create_user = mutation.InsertUser.Field()
    update_user = mutation.UpdateUser.Field()
    delete_user = mutation.DeleteUser.Field()
