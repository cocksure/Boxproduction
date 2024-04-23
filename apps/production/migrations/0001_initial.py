# Generated by Django 4.2.11 on 2024-04-23 09:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BoxModel",
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
                (
                    "name",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Название"
                    ),
                ),
            ],
            options={
                "verbose_name": "Модель коробки",
                "verbose_name_plural": "Модели коробок",
                "ordering": ["-created_time"],
            },
        ),
        migrations.CreateModel(
            name="BoxOrder",
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
                ("data", models.DateField(verbose_name="Дата")),
                (
                    "customer",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Клиент"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Одобрено", "Одобрено"),
                            ("Отклонено", "Отклонено"),
                            ("НОВАЯ", "НОВАЯ"),
                        ],
                        default="НОВАЯ",
                        max_length=20,
                        null=True,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "type_order",
                    models.CharField(max_length=100, verbose_name="Тип заказа"),
                ),
                (
                    "specification",
                    models.CharField(max_length=100, verbose_name="Спецификация"),
                ),
                (
                    "date_of_production",
                    models.DateField(verbose_name="Дата производства"),
                ),
            ],
            options={
                "verbose_name": "Заказ коробки",
                "verbose_name_plural": "Заказы коробок",
            },
        ),
        migrations.CreateModel(
            name="BoxOrderDetail",
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
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Количество",
                    ),
                ),
                (
                    "box_model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="production.boxmodel",
                        verbose_name="Модель коробки",
                    ),
                ),
                (
                    "box_order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="production.boxorder",
                        verbose_name="Заказ коробки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Детали заказа коробки",
                "verbose_name_plural": "Детали заказов коробок",
            },
        ),
        migrations.CreateModel(
            name="Process",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "verbose_name": "Процесс",
                "verbose_name_plural": "Процессы",
            },
        ),
        migrations.CreateModel(
            name="UploadImage",
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
                (
                    "photo",
                    models.ImageField(
                        default="no-image.png",
                        upload_to="box_photos/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["jpg", "jpeg", "png", "heic"]
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductionOrder",
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
                ("shipping_date", models.DateField(verbose_name="Дата доставки")),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Количество"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("in_progress", "In Progress"),
                            ("completed", "Completed"),
                            ("not_started", "Not Started"),
                        ],
                        default="not_started",
                        max_length=20,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "box_order_detail",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="production_orders",
                        to="production.boxorderdetail",
                        verbose_name="Детали заказа коробки",
                    ),
                ),
                (
                    "type_of_work",
                    models.ManyToManyField(
                        blank=True,
                        related_name="processes",
                        to="production.process",
                        verbose_name="Тип работы",
                    ),
                ),
            ],
            options={
                "verbose_name": "Производственный заказ",
                "verbose_name_plural": "Производственные заказы",
            },
        ),
    ]
