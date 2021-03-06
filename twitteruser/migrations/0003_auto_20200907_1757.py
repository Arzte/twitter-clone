# Generated by Django 3.1 on 2020-09-07 17:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0002_auto_20200907_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteruser',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='twitteruser_followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='twitteruser',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='twitteruser_following', to=settings.AUTH_USER_MODEL),
        ),
    ]
