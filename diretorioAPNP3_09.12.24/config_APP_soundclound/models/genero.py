from django.db import models

class Genero(models.Model):
    ELETRONICA = "Eletronica"
    METAL_MELODIC = "Metal Melodico"
    PAGODE = "Pagode"
    POP = "Pop"
    RAP = "Rap"
    ROCK = "Rock"

    GENERO_CHOICES = [
        (ELETRONICA, "Eletronica"),
        (METAL_MELODIC, "Metal Melodico"),
        (PAGODE, "Pagode"),
        (POP, "Pop"),
        (RAP, "Rap"),
        (ROCK, "Rock"),
    ]

    nome = models.CharField(max_length=50, choices=GENERO_CHOICES, default=POP)

    def __str__(self):
        return self.nome
