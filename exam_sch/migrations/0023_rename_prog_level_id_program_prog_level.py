# Generated by Django 4.2.7 on 2023-11-07 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_sch', '0022_program_prog_level_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='prog_level_id',
            new_name='prog_level',
        ),
    ]
