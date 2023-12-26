# Generated by Django 4.2.7 on 2023-12-15 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0002_alter_genre_name'),
        ('actors', '0002_alter_actor_birthday_alter_actor_name_and_more'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='actors.actor', verbose_name='Atores'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movies', to='genres.genre', verbose_name='Gênero'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_rating',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Avaliação IMDB'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data de lançamento'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='resume',
            field=models.TextField(blank=True, null=True, verbose_name='Resumo'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
    ]
