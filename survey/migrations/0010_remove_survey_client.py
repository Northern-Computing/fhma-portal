# Generated by Django 5.0.6 on 2024-11-24 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0009_remove_clientsurvey2024_helped_leave_home_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='client',
        ),
    ]