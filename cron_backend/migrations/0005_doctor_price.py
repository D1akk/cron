# Generated by Django 5.0 on 2023-12-23 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cron_backend", "0004_alter_doctor_clinic"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="price",
            field=models.FloatField(null=True),
        ),
    ]
