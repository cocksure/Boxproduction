# Generated by Django 5.0.2 on 2024-03-19 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_time", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_time", models.DateTimeField(auto_now=True)),
                ("full_name", models.CharField(max_length=100)),
            ],
            options={
                "ordering": ["-created_time"],
                "abstract": False,
            },
        ),
    ]