# Generated by Django 4.1.3 on 2022-12-19 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Uber", "0020_course_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="taxi",
            field=models.ForeignKey(
                blank=True,
                db_column="numImm",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Uber.taxi",
            ),
        ),
    ]
