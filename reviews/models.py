from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        verbose_name='Filme',
        related_name='reviews'
    )

    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação Mínima é 0 Estrela'),
            MaxValueValidator(5, 'Avaliação Máxima é 5 Estrelas')
        ],
    )

    comment = models.TextField(
        verbose_name='Cometário',
        blank=True, null=True
    )

    def __str__(self):
        return f'{self.movie} <> {self.stars}'
