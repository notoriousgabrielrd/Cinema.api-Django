# Generated by Django 4.0.6 on 2022-07-14 05:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('duration', models.CharField(max_length=20, null=True)),
                ('parental_rating', models.CharField(max_length=20)),
                ('sinopse', models.CharField(max_length=255)),
                ('imdb_rating', models.CharField(max_length=10)),
                ('release_date', models.DateField()),
                ('closing_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('genres', models.ManyToManyField(related_name='movies', to='genres.genre')),
            ],
        ),
    ]
