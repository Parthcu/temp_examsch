# Generated by Django 4.2.7 on 2023-11-07 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_sch', '0021_rename_program_type_program_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='prog_level_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam_sch.programme_level'),
        ),
    ]
