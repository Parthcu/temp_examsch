# Generated by Django 4.2.5 on 2023-11-06 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("exam_sch", "0014_alter_user_table_user_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_table",
            name="user_gender",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="exam_sch.gender"
            ),
        ),
    ]