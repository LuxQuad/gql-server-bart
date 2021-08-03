import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name: str):
        """
        hello

        :param info:
        :type name: str
        """

        return "Hello " + name
