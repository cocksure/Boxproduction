# Generated by Django 5.0.2 on 2024-03-04 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("production", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productionorder",
            name="box_order_detail",
        ),
        migrations.AddField(
            model_name="productionorder",
            name="box_order_detail",
            field=models.ManyToManyField(to="production.boxorderdetail"),
        ),
    ]
