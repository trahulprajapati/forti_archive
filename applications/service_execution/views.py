from django.shortcuts import render
from applications.mixins.archive_mixins import (
    CreateListServiceBase,
    RetrieveUpdateDeleteServiceBase,
)
from rest_framework.permissions import IsAuthenticated
from archive_auth.permissions import ArchiveExecutionPermission
from .models import Execution
from .serializers import ExecutionSerializer


# Create your views here.
class CreateListExecution(CreateListServiceBase):
    permission_classes = [IsAuthenticated, ArchiveExecutionPermission]
    model = Execution
    serializer_class = ExecutionSerializer

    def get_queryset(self):
        if self.request.user.is_admin:
            return Execution.objects.all()
        else:
            tables = self.request.user.table_user.all()
            executions = Execution.objects.filter(table__in=tables)
            return executions


class RetrieveUpdateDeleteExecution(RetrieveUpdateDeleteServiceBase):
    permission_classes = [IsAuthenticated, ArchiveExecutionPermission]
    model = Execution
    serializer_class = ExecutionSerializer
