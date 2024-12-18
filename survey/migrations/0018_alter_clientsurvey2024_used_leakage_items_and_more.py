# Generated by Django 5.0.6 on 2024-11-24 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0017_remove_clientsurvey2024__zipcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsurvey2024',
            name='used_leakage_items',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], help_text='Please select Yes or No', verbose_name='Have you ever used items to assist with leakage other than adult diapers, bladder pads/products (such as towels, sheets, washcloths etc.)?'),
        ),
        migrations.AlterField(
            model_name='clientsurvey2024',
            name='uti_lastyear',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], help_text='Please select Yes or No', verbose_name='Have you had a Urinary Tract Infection (UTI) in the last year?'),
        ),
    ]
