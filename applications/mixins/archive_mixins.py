from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CreateListServiceBase(
    mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView
):
    # serializer_class = ServiceSerializer
    # queryset = Service.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_serializer_class(self):
        return self.serializer_class

    def get_queryset(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # assert False, request.POST
        return self.create(request, *args, **kwargs)


class RetrieveUpdateDeleteServiceBase(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    permission_classes = [IsAuthenticated, IsAdminUser]

    # serializer_class = ServiceSerializer
    # queryset = Item.objects.all()
    def get_queryset(self):
        return self.model.objects.all()

    def get_serializer_class(self):
        return self.serializer_class

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
