from django.db import models
from django.contrib.auth.models import User
import json


class Carta(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cartas')
    titulo = models.CharField(max_length=255)
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cartas_recibidas')
    imagen = models.URLField(blank=True, null=True)
    contenido = models.TextField()
    posdata = models.TextField(blank=True, null=True)
    iframe = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    etiquetas = models.TextField(default="[]",blank=True,null=True)

    def save(self, *args, **kwargs):
        # Convertir la lista de etiquetas en un JSON antes de guardar
        if isinstance(self.etiquetas, list):
            self.etiquetas = json.dumps(self.etiquetas)
        super().save(*args, **kwargs)

    def get_etiquetas(self):
        # Convertir el JSON de vuelta a una lista al obtener las etiquetas
        return json.loads(self.etiquetas)

    def __str__(self):
        return self.titulo
