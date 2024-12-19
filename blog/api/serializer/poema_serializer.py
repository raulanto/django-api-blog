from rest_framework import serializers
from ...models import Poema



class PoemaSerializer(serializers.ModelSerializer):
    destinatario_nombre = serializers.CharField(source='destinatario.username', read_only=True)
    class Meta:
        model = Poema
        fields = ['id','autor', 'titulo', 'destinatario_nombre', 'imagen', 'contenido']





class PoemaCreaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poema
        fields = '__all__'
