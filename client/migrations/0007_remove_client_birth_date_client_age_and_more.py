# Generated by Django 5.0.6 on 2024-11-24 04:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_alter_areaserviced_name_alter_areaserviced_zipcode_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='client',
            name='age',
            field=models.IntegerField(blank=True, help_text='Please provide the clients age', null=True, verbose_name='Client Age'),
        ),
        migrations.AlterField(
            model_name='client',
            name='area_serviced',
            field=models.ForeignKey(help_text='Please select from the options provided', null=True, on_delete=django.db.models.deletion.CASCADE, to='client.areaserviced', verbose_name='Area or City'),
        ),
    ]