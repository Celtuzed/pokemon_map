# Generated by Django 3.1.14 on 2022-07-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_auto_20220708_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
