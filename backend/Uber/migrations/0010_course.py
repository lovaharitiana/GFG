# Generated by Django 4.1.3 on 2022-12-09 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Uber", "0009_categorie"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "numCrs",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("depart", models.CharField(max_length=30)),
                ("destination", models.CharField(max_length=30)),
            ],
        ),
    ]
