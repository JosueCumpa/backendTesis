# Generated by Django 4.2.7 on 2024-05-21 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaWeb', '0010_producto_tipopro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=150),
        ),
    ]
