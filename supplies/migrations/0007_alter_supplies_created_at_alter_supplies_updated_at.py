# Generated by Django 5.0.6 on 2024-11-29 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0006_remove_suppliesorder_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplies',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='supplies',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
