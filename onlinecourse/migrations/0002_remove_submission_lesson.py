# Generated by Django 3.1.3 on 2021-07-31 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='lesson',
        ),
    ]
