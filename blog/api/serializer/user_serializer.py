from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para manejar datos del modelo User.
    """

    class Meta:
        model = User
        fields = ('id', 'username')
        extra_kwargs = {
            'password': {'write_only': True},  # Oculta la contraseña al leer
        }

    def create(self, validated_data):
        """
        Crea un usuario con la contraseña encriptada.
        """
        user = User.objects.create_user(**validated_data)
        return user
