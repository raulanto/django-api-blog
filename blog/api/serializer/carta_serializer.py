from rest_framework import serializers
from ...models import Carta


class CartaSerializer(serializers.ModelSerializer):
    destinatario_nombre = serializers.CharField(source='destinatario.username', read_only=True)
    class Meta:
        model = Carta
        fields = ['id','autor', 'titulo', 'destinatario_nombre', 'imagen', 'contenido', 'posdata', 'iframe',
                  'fecha_creacion', 'etiquetas','destinatario']

class CartaCreaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carta
        fields = '__all__'
