import graphene
import School.schema as School_schema


# to add multiple schema add in Query class separated by comma
class Query(School_schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
