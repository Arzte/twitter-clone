# Generated by Django 3.1 on 2020-09-07 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20200907_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='mention',
            new_name='mentioned_by',
        ),
    ]
