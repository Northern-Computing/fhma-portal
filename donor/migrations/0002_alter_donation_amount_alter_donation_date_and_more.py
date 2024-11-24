# Generated by Django 5.0.6 on 2024-11-23 03:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='amount',
            field=models.DecimalField(decimal_places=2, help_text='Please provide the donation amount', max_digits=10, verbose_name='Donation Amount'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='date',
            field=models.DateField(help_text='Please provide the donation date', verbose_name='Donation Date'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(help_text='Please select the donor associated with the donation', on_delete=django.db.models.deletion.CASCADE, to='donor.donor', verbose_name='Donor associated with the donation'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='address',
            field=models.TextField(blank=True, help_text='Please provide the donor address', null=True, verbose_name='Donor Address (Optional)'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='city',
            field=models.CharField(blank=True, help_text='Please provide the donor city', max_length=50, null=True, verbose_name='Donor City (Optional)'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='country',
            field=models.CharField(blank=True, help_text='Please provide the donor country', max_length=50, null=True, verbose_name='Donor Country (Optional)'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='email',
            field=models.EmailField(blank=True, help_text='Please provide the donor email', max_length=254, null=True, verbose_name='Donor Email (Optional)'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='last_donated',
            field=models.DateField(blank=True, help_text='Please provide the last donation date', null=True, verbose_name='Last Donation Date (Optional)'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='name',
            field=models.CharField(help_text='Please provide the donor name', max_length=100, verbose_name='Donor Name'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='phone',
            field=models.CharField(blank=True, help_text='Please provide the donor phone number', max_length=15, null=True, verbose_name='Donor Phone (Optional)'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='state',
            field=models.CharField(blank=True, help_text='Please provide the donor state', max_length=50, null=True, verbose_name='Donor State (Optional)'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='zip',
            field=models.CharField(blank=True, help_text='Please provide the donor zip', max_length=10, null=True, verbose_name='Donor Zip (Optional)'),
        ),
    ]