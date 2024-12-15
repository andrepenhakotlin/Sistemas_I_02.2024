from django.db import models
from .genero import Genero

class Playlist(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(min_length=10, null=True, blank=True)
    data_criacao = models.DateField(auto_now_add=True)
    nr_likes = models.IntegerField(default=0)
    duracao = models.DurationField()

    def __str__(self):
        return self.titulo
