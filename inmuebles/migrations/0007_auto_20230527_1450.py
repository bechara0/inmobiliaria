# Generated by Django 3.2.19 on 2023-05-27 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0006_auto_20230526_2005'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Características',
            new_name='Caracteristicas',
        ),
        migrations.RenameField(
            model_name='inmueble',
            old_name='características',
            new_name='caracteristicas',
        ),
    ]
