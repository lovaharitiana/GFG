# Generated by Django 4.1.3 on 2022-11-27 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Uber", "0006_agence"),
    ]

    operations = [
        migrations.CreateModel(
            name="Capacite",
            fields=[
                ("numCap", models.IntegerField(primary_key=True, serialize=False)),
                ("droit", models.IntegerField()),
                ("date_certificat", models.DateField()),
            ],
        ),
    ]
