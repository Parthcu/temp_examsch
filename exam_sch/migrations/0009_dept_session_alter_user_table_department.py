# Generated by Django 4.2.5 on 2023-11-06 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("exam_sch", "0008_rename_user_role_id_user_table_user_role"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dept",
            fields=[
                ("dept_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "dept_name",
                    models.CharField(
                        choices=[
                            ("online", "Online"),
                            ("odl", "Online-Distance Learning"),
                            ("regular", "Regular"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "dept_status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Session",
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
                ("start_year", models.PositiveIntegerField()),
                ("end_year", models.PositiveIntegerField()),
                (
                    "start_month",
                    models.CharField(
                        choices=[("01", "January"), ("07", "July")], max_length=3
                    ),
                ),
                (
                    "end_month",
                    models.CharField(
                        choices=[("05", "May"), ("12", "December")], max_length=3
                    ),
                ),
                (
                    "session_code",
                    models.CharField(editable=False, max_length=6, unique=True),
                ),
                (
                    "dept_name",
                    models.ForeignKey(
                        default=3,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exam_sch.dept",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="user_table",
            name="department",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="exam_sch.dept",
            ),
        ),
    ]