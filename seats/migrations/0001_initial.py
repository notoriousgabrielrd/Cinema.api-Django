# Generated by Django 4.0.6 on 2022-07-21 02:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie_theaters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('row', models.CharField(max_length=20)),
                ('seat', models.CharField(max_length=20)),
                ('status_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ticket_seat_id', models.UUIDField(default=uuid.uuid4)),
                ('movie_theater', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='seats', to='movie_theaters.movietheater')),
            ],
        ),
        migrations.CreateModel(
            name='SeatMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seatMap', models.ManyToManyField(related_name='seatMap', to='seats.seat')),
            ],
        ),
    ]
