# Generated by Django 4.1.3 on 2022-11-28 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Uber", "0008_permi"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categorie",
            fields=[
                (
                    "numCat",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("type", models.CharField(max_length=5)),
            ],
        ),
    ]
