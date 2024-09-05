# Generated by Django 4.2 on 2024-09-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Climatologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('temperatura', models.FloatField()),
                ('humedad', models.FloatField()),
                ('presion', models.FloatField()),
                ('velocidad_viento', models.FloatField()),
            ],
        ),
    ]