# Generated by Django 4.2.7 on 2023-12-15 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genres', '0001_initial'),
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('resume', models.TextField(blank=True, null=True)),
                ('imdb_rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('actors', models.ManyToManyField(related_name='movies', to='actors.actor')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movies', to='genres.genre')),
            ],
        ),
    ]