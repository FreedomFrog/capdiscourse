# Generated by Django 2.0.6 on 2018-06-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0003_corpus_binary_sentiment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corpus',
            name='binary_sentiment',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]