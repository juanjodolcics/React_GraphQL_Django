import graphene
from graphene_django.types import DjangoObjectType
from .models import Cliente


class ClienteType(DjangoObjectType):
    class Meta:
        model = Cliente


class Query(object):
    all_clientes = graphene.List(ClienteType)

    def resolve_all_clientes(self, info, **kwargs):
        return Cliente.objects.all()