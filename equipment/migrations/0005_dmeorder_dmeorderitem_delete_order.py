# Generated by Django 5.0.6 on 2024-11-30 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_client_gender'),
        ('equipment', '0004_alter_equipment_barcode_alter_equipment_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DMEOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('RT', 'Rented'), ('RU', 'Returned')], default='RT', help_text='Please select the order status', max_length=2, verbose_name='Order Status')),
                ('rental_date', models.DateTimeField(help_text='Please provide date the equipment was rented', verbose_name='Rental Date')),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(help_text='Please select the client associated with the order', on_delete=django.db.models.deletion.CASCADE, to='client.client', verbose_name='Client associated with the order')),
            ],
        ),
        migrations.CreateModel(
            name='DMEOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, help_text='Please provide the equipment quantity', verbose_name='Equipment Quantity')),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('equipment', models.ForeignKey(help_text='Please select the equipment associated with the order', on_delete=django.db.models.deletion.CASCADE, to='equipment.equipment', verbose_name='Equipment associated with the order')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='equipment.dmeorder')),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]