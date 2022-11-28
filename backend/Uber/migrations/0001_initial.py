# Generated by Django 4.1.3 on 2022-11-22 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chauffeur',
            fields=[
                ('numChf', models.AutoField(primary_key=True, serialize=False)),
                ('nomChf', models.CharField(max_length=30)),
                ('prenomChf', models.CharField(max_length=20)),
                ('date_naissance', models.DateField()),
                ('lieu_naissance', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=20)),
                ('profession', models.CharField(max_length=20)),
            ],
        ),
    ]
