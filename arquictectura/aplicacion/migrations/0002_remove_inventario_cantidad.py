# Generated by Django 5.0.1 on 2024-01-22 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario',
            name='cantidad',
        ),
    ]
