# Generated by Django 5.0.1 on 2024-01-22 04:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('cantidad', models.IntegerField()),
                ('Ciudad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RolPersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('ubicacion', models.CharField(max_length=50)),
                ('inventario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='almacen_inventario', to='aplicacion.inventario')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('cantidad', models.IntegerField()),
                ('estado', models.CharField(max_length=30)),
                ('novedad', models.CharField(max_length=50, null=True)),
                ('fechaEntrada', models.DateField()),
                ('fechaCaducidad', models.DateField(null=True)),
                ('via_administrativa', models.CharField(max_length=30, null=True)),
                ('material', models.CharField(max_length=30, null=True)),
                ('instrucciones_almacenamiento', models.CharField(max_length=100, null=True)),
                ('instrucciones_uso', models.CharField(max_length=100, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto_categoria', to='aplicacion.categoriaproducto')),
                ('inventario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='producto_inventario', to='aplicacion.inventario')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('edad', models.IntegerField()),
                ('inventario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personal_inventario', to='aplicacion.inventario')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personal_rol', to='aplicacion.rolpersona')),
            ],
        ),
    ]
