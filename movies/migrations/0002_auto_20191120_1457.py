# Generated by Django 2.2.7 on 2019-11-20 05:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]