# Generated by Django 4.1.3 on 2022-12-14 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Uber", "0011_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="assurance",
            name="taxi",
            field=models.ForeignKey(
                blank=True,
                db_column="numImm",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Uber.taxi",
            ),
        ),
        migrations.AddField(
            model_name="taxi",
            name="carte_grise",
            field=models.OneToOneField(
                blank=True,
                db_column="numSerie",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Uber.carte_grise",
            ),
        ),
    ]