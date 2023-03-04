# Generated by Django 4.1.3 on 2023-02-25 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boos', '0010_remove_employee_job_job_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='project',
        ),
        migrations.AddField(
            model_name='department',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='boos.job'),
        ),
        migrations.AlterField(
            model_name='job',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='boos.employee'),
        ),
    ]
