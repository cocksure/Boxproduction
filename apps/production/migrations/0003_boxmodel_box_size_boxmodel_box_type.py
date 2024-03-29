# Generated by Django 5.0.2 on 2024-03-20 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0003_boxsize_boxtype"),
        ("production", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="boxmodel",
            name="box_size",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="info.boxsize",
            ),
        ),
        migrations.AddField(
            model_name="boxmodel",
            name="box_type",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="info.boxtype",
            ),
        ),
    ]
