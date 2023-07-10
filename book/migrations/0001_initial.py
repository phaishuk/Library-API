# Generated by Django 4.2.3 on 2023-07-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
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
                ("title", models.CharField(max_length=150)),
                ("author", models.CharField(max_length=150)),
                (
                    "cover",
                    models.CharField(
                        choices=[("Hard", "Hard"), ("Soft", "Soft")], max_length=10
                    ),
                ),
                ("inventory", models.PositiveIntegerField()),
                ("daily_fee", models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
