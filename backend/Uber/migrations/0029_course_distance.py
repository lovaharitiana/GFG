# Generated by Django 4.1.3 on 2023-01-04 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Uber", "0028_remove_course_distance"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="distance",
            field=models.FloatField(default=0.0),
        ),
    ]