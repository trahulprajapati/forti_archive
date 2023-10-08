from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import UserSerializer, EmptySerializer, RegisterSerializer
from rest_framework import generics, permissions, mixins
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": RegisterSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "message": "User Created Successfully.  Now perform Login to get your token",
            }
        )


# class AddRoleView(ViewSet):
#     permission_classes = [IsAdminUser]
#     serializer_class = RegisterSerializer
#     queryset = User.objects.select_related('table_user').all()
#
#     def partial_update(self, request, *args, **kwargs):
#         instance = self.queryset.get(pk=kwargs.get('pk'))
#         serializer = self.serializer_class(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# views.py
class RegisterUserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
