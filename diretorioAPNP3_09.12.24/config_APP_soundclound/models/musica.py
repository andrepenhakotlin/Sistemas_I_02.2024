from django.db import models
from .genero import Genero

class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    letra = models.TextField(min_length=10, blank=True, null=True)
    data_upload = models.DateField(auto_now_add=True)
    nr_likes = models.IntegerField(default=0)
    duracao = models.DurationField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    album = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
