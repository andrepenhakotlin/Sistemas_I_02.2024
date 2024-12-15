from django.db import models
from .genero import Genero

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    nome_artistico = models.CharField(max_length=50)
    biografia = models.TextField(max_length=500, blank=True, null=True)
    seguidores = models.IntegerField(default=0)
    nr_albuns = models.IntegerField(default=0)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    data_criacao = models.DateField(auto_now_add=True)
    nr_plays = models.IntegerField()

    def __str__(self):
        return self.nome_artistico
