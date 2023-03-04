# Generated by Django 4.1.3 on 2023-02-25 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boos', '0013_remove_project_employee_project_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gander',
            field=models.CharField(choices=[(1, 'male'), (2, 'female')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='boos.employee'),
        ),
        migrations.AlterField(
            model_name='project',
            name='employee',
            field=models.ManyToManyField(null=True, to='boos.employee'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]