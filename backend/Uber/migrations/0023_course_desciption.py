# Generated by Django 4.1.3 on 2022-12-22 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Uber", "0022_course_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="desciption",
            field=models.CharField(default="Description de la course", max_length=255),
        ),
    ]
