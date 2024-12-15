from django.db import models
from datetime import timedelta
from .genero import Genero
from .artista import Artista
from django.core.validators import MinLengthValidator, MinValueValidator

# https://docs.djangoproject.com/en/5.1/topics/db/models/


class Musica(models.Model):
    titulo = models.CharField(max_length=100, validators=[MinLengthValidator(1)], verbose_name='Titulo')
    letra = models.TextField(validators=[MinLengthValidator(10)], null=True, blank=True, verbose_name='Letra')
    data_upload = models.DateField(auto_now_add=True, verbose_name='Data de Upload')
    nr-likes = models.IntegerField(default=0, validators=[MinValueValidator(0)], verbose_name='Numero de likes')
    duracao = models.DurationField(verbose_name='Duracao')
    genero = models.CharField(max_length=20, choices=Genero.choices, verbose_name='Genero')
    album = models.CharField(max_length=100, validators=[MinLengthValidator(1)], verbose_name='Album')
    nr_plays = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Numero de Plays')
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, verbose_name='Artista')
    
    def like(self):
        self.nr_likes += 1
        self.save()
        
    def play(self):
        self.nr_play += 1
        self.save()
        
    def __str__(self):
        return self.titulo
    