# Generated by Django 4.1.1 on 2022-10-18 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_manager', '0008_alter_executionresults_results'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExecutionEvents',
        ),
        migrations.DeleteModel(
            name='ExecutionResults',
        ),
    ]
