# Generated by Django 4.1.3 on 2023-03-04 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boos', '0016_alter_employee_gander'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='job',
        ),
        migrations.AddField(
            model_name='job',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='boos.department'),
        ),
    ]
