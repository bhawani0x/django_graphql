import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import *
from datetime import datetime


class ClassType(DjangoObjectType):
    # Describe the data that is to be formatted into GraphQL fields
    class Meta:
        model = Class
        field = "__all__"


class StudentType(DjangoObjectType):
    # Describe the data that is to be formatted into GraphQL fields
    class Meta:
        model = Student

    isAdult = graphene.String()

    def resolve_isAdult(self, info, **kwargs):
        dob_date = self.dob
        current_date = datetime.now()
        age = current_date.year - dob_date.year - (
                (current_date.month, current_date.day) < (dob_date.month, dob_date.day))

        if age >= 18:
            return "Adult"
        else:
            return "Child"


class Query(graphene.ObjectType):
    # query ContactType to get list of contacts
    allClass = graphene.List(ClassType)

    def resolve_allClass(root, info):
        # We can easily optimize query count in the resolve method
        return Class.objects.all()

    # we can also write it without resolver
    allStudent = DjangoListField(StudentType)
    student = graphene.Field(StudentType, id=graphene.Int())

    def resolve_student(root, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Student.objects.get(pk=id)
        return None


schema = graphene.Schema(query=Query)
