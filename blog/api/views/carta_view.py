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


from ..serializer.carta_serializer import CartaSerializer,CartaCreaterSerializer
from ...models.Carta import Carta
class CartaViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = Carta.objects.all()

    serializer_class = CartaSerializer
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



class CartaCreateAPIView(CreateAPIView):
    queryset = Carta.objects.all()
    serializer_class = CartaCreaterSerializer
    permission_classes = [AllowAny]


