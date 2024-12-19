from django.db import models
from django.contrib.auth.models import User

class Poema(models.Model):
    titulo = models.CharField(max_length=200, help_text="Título del poema")
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='poemas', help_text="Usuario que creó el poema")
    contenido = models.TextField(help_text="Contenido del poema")
    creado_en = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación")
    actualizado_en = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última actualización")
    imagen = models.URLField(blank=True, null=True,default="~/assets/img/fondo2.webp")

    class Meta:
        verbose_name = "Poema"
        verbose_name_plural = "Poemas"
        ordering = ['-creado_en']

    def __str__(self):
        return f"{self.titulo} por {self.autor.username}"
