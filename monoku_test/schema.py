import graphene
import songs.schema


class Query(songs.schema.Query, graphene.ObjectType):
    pass


class Mutation(songs.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
