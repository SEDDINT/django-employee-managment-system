# Generated by Django 4.1.3 on 2023-02-25 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boos', '0006_alter_employee_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='job',
        ),
        migrations.AddField(
            model_name='employee',
            name='postion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='boos.employee'),
        ),
    ]
