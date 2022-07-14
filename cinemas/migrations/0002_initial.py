# Generated by Django 4.0.6 on 2022-07-14 05:40


from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cinemas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='user',
            field=models.ManyToManyField(null=True, related_name='cinemas', to=settings.AUTH_USER_MODEL),
        ),
    ]
