# Generated by Django 5.1.3 on 2024-11-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Division",
            fields=[
                ("division_id", models.IntegerField(primary_key=True, serialize=False)),
                ("division_name", models.CharField(max_length=4, unique=True)),
            ],
            options={
                "db_table": "division",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Driver",
            fields=[
                (
                    "driver_id",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
            ],
            options={
                "db_table": "driver",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Equipment",
            fields=[
                (
                    "equipment_id",
                    models.CharField(max_length=4, primary_key=True, serialize=False),
                ),
                ("equipment_type", models.CharField(max_length=10)),
                ("equipment_sort", models.CharField(max_length=10)),
                ("status", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "equipment",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Master",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "master",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Site",
            fields=[
                ("site_id", models.IntegerField(primary_key=True, serialize=False)),
                ("capacity", models.IntegerField()),
                ("current_quantity", models.IntegerField()),
            ],
            options={
                "db_table": "site",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "transaction_id",
                    models.FloatField(primary_key=True, serialize=False),
                ),
                ("driver_id", models.CharField(max_length=10)),
                ("timestamp", models.IntegerField()),
                ("details", models.TextField()),
            ],
            options={
                "db_table": "transaction",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Yard",
            fields=[
                (
                    "yard_id",
                    models.CharField(max_length=5, primary_key=True, serialize=False),
                ),
            ],
            options={
                "db_table": "yard",
                "managed": False,
            },
        ),
    ]
