# Generated by Django 4.2.7 on 2024-05-21 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaWeb', '0009_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='tipoPro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SistemaWeb.tipoproducto'),
        ),
    ]