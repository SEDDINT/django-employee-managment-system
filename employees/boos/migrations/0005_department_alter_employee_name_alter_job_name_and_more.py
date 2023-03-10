# Generated by Django 4.1.3 on 2023-02-25 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boos', '0004_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
