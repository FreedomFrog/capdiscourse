# Generated by Django 2.0.6 on 2018-06-12 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0010_topic_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='text',
        ),
        migrations.AddField(
            model_name='topic',
            name='text',
            field=models.ManyToManyField(to='classifier.UserText'),
        ),
    ]
