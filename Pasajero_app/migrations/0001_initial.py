# Generated by Django 5.1.2 on 2024-12-05 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('Id_Pasagero', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Numero_Documento', models.IntegerField()),
                ('Nacionalidad', models.CharField(max_length=100)),
                ('Fecha_de_Nacimiento', models.CharField(max_length=100)),
                ('Telefono', models.CharField(max_length=100)),
            ],
        ),
    ]