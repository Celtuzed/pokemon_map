# Generated by Django 3.1.14 on 2022-07-15 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0012_pokemon_evolution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='evolution',
            new_name='previous_evolution',
        ),
    ]
