from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)


from ..serializer.poema_serializer import PoemaCreaterSerializer,PoemaSerializer
from ...models.Poema import Poema
class PoemaViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = Poema.objects.all()

    serializer_class = PoemaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['autor','id']

    # def update(self, request, *args, **kwargs):
    #     self.serializer_class = ProductoUpdateSerializer
    #     response = super().update(request, *args, **kwargs)
    #
    #     # # Registra el cambio
    #     # objeto = self.get_object()
    #     # mensaje = "Producto actualizado"
    #     # registrarCambio(request, objeto, mensaje)
    #     #
    #     # return response



class PoemaCreateAPIView(CreateAPIView):
    queryset = Poema.objects.all()
    serializer_class = PoemaCreaterSerializer
    permission_classes = [AllowAny]


