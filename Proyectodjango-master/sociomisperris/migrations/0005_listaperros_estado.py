# Generated by Django 4.2.1 on 2023-05-27 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sociomisperris', '0004_remove_listaperros_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='listaperros',
            name='estado',
            field=models.IntegerField(choices=[(1, 'Disponible'), (2, 'Rescatado'), (3, 'Adoptado'), (4, 'En tratamiento medicos')], default=1),
            preserve_default=False,
        ),
    ]
