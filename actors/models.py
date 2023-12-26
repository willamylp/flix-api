from django.db import models

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRA', 'Brasil'),
)

class Actor(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Nome'
    )
    birthday = models.DateField(
        blank=True, null=True,
        verbose_name='Data de nascimento'
    )
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        verbose_name='Nacionalidade'
    )

    def __str__(self):
        return self.name
    