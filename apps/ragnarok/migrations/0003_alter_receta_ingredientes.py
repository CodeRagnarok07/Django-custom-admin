# Generated by Django 5.0.1 on 2024-01-28 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ragnarok', '0002_alter_cantidadingerediente_ingrediente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='ingredientes',
            field=models.ManyToManyField(to='ragnarok.cantidadingerediente'),
        ),
    ]
