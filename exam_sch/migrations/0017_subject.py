# Generated by Django 4.2.5 on 2023-11-07 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exam_sch", "0016_program_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subject",
            fields=[
                ("subject_id", models.AutoField(primary_key=True, serialize=False)),
                ("subject_name", models.CharField(max_length=255, unique=True)),
                ("subject_code", models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
