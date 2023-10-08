from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import (
    ServiceSerializer,
    SchemaSerializer,
    DbServerSerializer,
    TableSerializer,
    PolicySerializer,
)
from .models import Service, DbServer, Schema, Tables, Policy
from archive_auth.permissions import (
    PolicyConfigurePermission,
    BaseArchivePermission,
    ArchiveTablePermission,
)
from applications.mixins.archive_mixins import (
    CreateListServiceBase,
    RetrieveUpdateDeleteServiceBase,
)


class CreateListService(CreateListServiceBase):
    model = Service
    serializer_class = ServiceSerializer


class RetrieveUpdateDeleteService(RetrieveUpdateDeleteServiceBase):
    model = Service
    serializer_class = ServiceSerializer


class CreateListDbserver(CreateListServiceBase):
    model = DbServer
    serializer_class = DbServerSerializer


class RetrieveUpdateDeleteDbserver(RetrieveUpdateDeleteServiceBase):
    model = DbServer
    serializer_class = DbServerSerializer


class CreateListSchema(CreateListServiceBase):
    model = Schema
    serializer_class = SchemaSerializer


class RetrieveUpdateDeleteSchema(RetrieveUpdateDeleteServiceBase):
    model = Schema
    serializer_class = SchemaSerializer


class CreateListTable(CreateListServiceBase):
    permission_classes = [IsAuthenticated, BaseArchivePermission]
    model = Tables
    serializer_class = TableSerializer


class RetrieveUpdateDeleteTable(RetrieveUpdateDeleteServiceBase):
    permission_classes = [IsAuthenticated, ArchiveTablePermission]
    model = Tables
    serializer_class = TableSerializer


class CreateListPolicy(CreateListServiceBase):
    permission_classes = [IsAuthenticated, BaseArchivePermission]
    model = Policy
    serializer_class = PolicySerializer


class RetrieveUpdateDeletePolicy(RetrieveUpdateDeleteServiceBase):
    permission_classes = [IsAuthenticated, PolicyConfigurePermission]
    model = Policy
    serializer_class = PolicySerializer
