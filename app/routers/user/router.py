from fastapi import APIRouter
import graphene
from starlette.graphql import GraphQLApp

from app import models
from app.resolvers import user

router = APIRouter(
    prefix="",
    tags=["사용자"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

router.add_route("/", GraphQLApp(schema=graphene.Schema(query=user.Query, mutation=user.Mutation, types=[models.user.User])))
