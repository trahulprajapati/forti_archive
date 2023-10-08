from rest_framework import permissions
from applications.service_catalog.models import Tables


class BaseArchivePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.is_admin:
            return True
        if view.action in ["delete", "create", "destroy"]:
            return False
        else:
            is_valid_user = Tables.objects.filter(users=request.user).exists()
            return is_valid_user


class PolicyConfigurePermission(BaseArchivePermission):
    """
    Global permission check for user has access on Policy table
    """

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated():
            return False

        if request.user.is_admin:
            return True

        if view.action in [
            "update",
            "put",
            "partial_update",
            "patch",
            "get",
            "retrieve",
        ]:
            # check if user has access on table
            last = request.user.table_user.filter(pk=obj.table.id).exists()
            return last
        else:
            return False


class ArchiveExecutionPermission(BaseArchivePermission):
    """
    Global permission check for user can check for archive
    """

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated():
            return False

        if request.user.is_admin:
            return True
        if view.action in ["retrieve", "get"]:
            # check if user has access on table
            last = request.user.table_user.filter(pk=obj.table.id).exists()
            return last
        else:
            return False


class ArchiveTablePermission(BaseArchivePermission):
    """
    Global permission check for user can check for archive
    """

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated():
            return False

        if request.user.is_admin:
            return True

        if view.action in ["retrieve", "get"]:
            # check if user has access on table
            last = request.user.table_user.filter(id=obj.id).exists()
            return last
        else:
            return False
