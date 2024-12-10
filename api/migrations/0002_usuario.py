# Generated by Django 5.1.4 on 2024-12-05 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('numero_ficha', models.IntegerField(unique=True)),
                ('formacion', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
            ],
        ),
    ]