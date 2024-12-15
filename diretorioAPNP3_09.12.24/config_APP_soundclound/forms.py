from django import forms
from .models.artista import Artista

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nome', 'nome_artistico', 'biografia', 'seguidores', 'nr_albuns', 'genero', 'nr_plays']
