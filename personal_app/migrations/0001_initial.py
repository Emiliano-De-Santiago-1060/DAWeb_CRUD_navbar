# Generated by Django 5.1.2 on 2024-11-22 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.TextField(max_length=300)),
                ('direccion', models.TextField(max_length=100)),
                ('telefono', models.TextField(max_length=100)),
                ('cargo', models.TextField(max_length=100)),
                ('sueldo', models.FloatField(max_length=100)),
            ],
        ),
    ]
