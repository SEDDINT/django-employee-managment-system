# Generated by Django 4.1.3 on 2023-02-25 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boos', '0007_remove_employee_job_employee_postion_job_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='postion',
            new_name='job',
        ),
        migrations.RemoveField(
            model_name='job',
            name='employee',
        ),
    ]
