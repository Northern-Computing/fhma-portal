# Generated by Django 5.0.6 on 2024-10-21 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(upload_to='equipment/images')),
                ('barcode', models.CharField(max_length=100)),
            ],
        ),
    ]
