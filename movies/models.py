from django.db import models
from actors.models import Actor
from genres.models import Genre

class Movie(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Título'
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name='movies',
        verbose_name='Gênero'
    )
    release_date = models.DateField(
        null=True, blank=True, 
        verbose_name='Data de lançamento'
    )
    actors = models.ManyToManyField(
        Actor,
        related_name='movies',
        verbose_name='Atores'
    )
    resume = models.TextField(
        max_length=1000,
        null=True, blank=True,
        verbose_name='Resumo'
    )
    
    def __str__(self):
        return self.title