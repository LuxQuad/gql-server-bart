from fastapi import APIRouter
from starlette.graphql import GraphQLApp
import graphene


from app.resolvers import user

router = APIRouter(
    prefix="",
    tags=["사용자"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

router.add_route("/", GraphQLApp(schema=graphene.Schema(query=user.Query)))