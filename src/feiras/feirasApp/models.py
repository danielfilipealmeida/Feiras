from django.db import models
from django.core.validators import MaxValueValidator

class Local(models.Model):
    local = models.CharField(max_length=100)
    coordenadas = models.CharField(max_length=100)

    def __str__(self):
        return self.local

    


class Feira(models.Model):
    class DiaSemana(models.IntegerChoices):
        DOMINGO = 1
        SEGUNDA = 2
        TERCA = 3
        QUARTA = 4
        QUINTA = 5
        SEXTA = 6
        SABADO = 7

    class Semana(models.IntegerChoices):
        TODAS = 0
        PRIMEIRA = 1
        SEGUNDA = 2
        TERCEIRA = 3
        QUARTA = 4
        QUINTA = 5

    nome = models.CharField(max_length=100)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    semana = models.PositiveSmallIntegerField(choices=Semana.choices, null=True)
    dia = models.IntegerField(choices=DiaSemana.choices, null=True)
    inicio = models.TimeField(null=True)
    fim = models.TimeField(null=True)
    morada = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.nome