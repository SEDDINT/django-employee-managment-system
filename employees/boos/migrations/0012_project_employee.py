# Generated by Django 4.1.3 on 2023-02-25 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boos', '0011_remove_employee_project_department_job_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='boos.employee'),
        ),
    ]
