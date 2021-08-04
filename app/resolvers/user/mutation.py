from graphene import String, Mutation, Boolean

from app.schemas import user

class InsertUser(Mutation):
    class Arguments:
        username = String(required=True)
        email = String(required=True)
        password = String(required=True)


    username = Field(lambda: user.UserModel)