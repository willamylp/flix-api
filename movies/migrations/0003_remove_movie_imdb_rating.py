# Generated by Django 4.2.7 on 2023-12-15 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_actors_alter_movie_genre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='imdb_rating',
        ),
    ]
