from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

# Swagger
from .swagger import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    #swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include("School.urls"))
]
