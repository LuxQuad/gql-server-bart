from fastapi import APIRouter
from starlette.graphql import GraphQLApp
import graphene


from app.resolver import hello

router = APIRouter(
    prefix="",
    tags=["Hello"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

router.add_route("/", GraphQLApp(schema=graphene.Schema(query=hello.Query)))