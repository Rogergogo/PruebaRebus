# Generated by Django 4.0.5 on 2022-07-06 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fifa', '0005_person_staff_remove_player_birthday_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Persona', 'verbose_name_plural': 'Persona'},
        ),
        migrations.AlterModelTable(
            name='person',
            table='Person',
        ),
    ]