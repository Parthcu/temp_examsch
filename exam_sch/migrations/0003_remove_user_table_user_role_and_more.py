# Generated by Django 4.2.5 on 2023-11-03 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("exam_sch", "0002_remove_roles_password_alter_roles_role_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user_table",
            name="user_role",
        ),
        migrations.AlterField(
            model_name="user_table",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="user_table",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users_with_rolename",
                to="exam_sch.roles",
            ),
        ),
    ]
