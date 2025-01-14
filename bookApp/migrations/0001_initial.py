# Generated by Django 5.0.7 on 2024-08-14 21:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genres",
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
                ("genre", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="LoginTable",
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
                ("username", models.CharField(max_length=200, null=True)),
                ("email", models.EmailField(max_length=200, null=True)),
                ("password", models.CharField(max_length=200, null=True)),
                ("cpassword", models.CharField(max_length=200, null=True)),
                ("type", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                ("username", models.CharField(max_length=200, null=True)),
                ("email", models.EmailField(max_length=200, null=True)),
                ("password", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=200, null=True)),
                ("author", models.CharField(max_length=200, null=True)),
                ("price", models.IntegerField(null=True)),
                ("dPrice", models.IntegerField(null=True)),
                ("dPercent", models.IntegerField(null=True)),
                ("pages", models.IntegerField(null=True)),
                ("language", models.CharField(max_length=200, null=True)),
                ("image", models.ImageField(null=True, upload_to="book_media")),
                ("quantity", models.PositiveIntegerField(default=0)),
                ("summary", models.TextField(max_length=5000, null=True)),
                (
                    "genre",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bookApp.genres",
                    ),
                ),
            ],
        ),
    ]
