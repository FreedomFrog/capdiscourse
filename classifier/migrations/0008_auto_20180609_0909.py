# Generated by Django 2.0.6 on 2018-06-09 16:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classifier', '0007_interests'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Interests',
            new_name='Topic',
        ),
    ]
