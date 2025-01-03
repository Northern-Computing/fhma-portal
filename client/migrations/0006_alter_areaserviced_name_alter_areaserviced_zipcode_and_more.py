# Generated by Django 5.0.6 on 2024-11-23 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_client_below_poverty_line_client_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areaserviced',
            name='name',
            field=models.CharField(help_text='Please provide the area or city name', max_length=200, verbose_name='Area or City Name'),
        ),
        migrations.AlterField(
            model_name='areaserviced',
            name='zipcode',
            field=models.CharField(help_text='Please provide the area or city zipcode', max_length=200, verbose_name='Area or City Zipcode'),
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, help_text='Please provide the clients address', max_length=200, null=True, verbose_name='Client Address (Optional)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='birth_date',
            field=models.DateField(blank=True, help_text='Please provide the clients date of birth', null=True, verbose_name='Client Date of Birth (Optional)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(blank=True, help_text='Please provide the clients city', max_length=200, null=True, verbose_name='Client City (Optional)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='country',
            field=models.CharField(blank=True, help_text='Please provide the clients country', max_length=200, null=True, verbose_name='Client Country (Optional)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, help_text='Please provide the clients email', max_length=200, null=True, verbose_name='Client Email (Optional)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(help_text='Please provide the clients name', max_length=200, verbose_name='Client Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, help_text='Please provide the clients phone number', max_length=20, null=True, verbose_name='Client Phone (Optional)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='state',
            field=models.CharField(blank=True, help_text='Please provide the clients state', max_length=200, null=True, verbose_name='Client State (Optional)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='zipcode',
            field=models.CharField(blank=True, help_text='Please provide the clients zipcode', max_length=200, null=True, verbose_name='Client Zipcode (Optional)'),
        ),
    ]
