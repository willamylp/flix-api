from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Nome'
    )

    def __str__(self):
        return self.name

