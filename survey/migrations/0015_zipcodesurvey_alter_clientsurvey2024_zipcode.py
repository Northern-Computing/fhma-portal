# Generated by Django 5.0.6 on 2024-11-24 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0014_delete_medicaltreatmentquestion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZipcodeSurvey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', models.CharField(blank=True, help_text='Please provide your zipcode', max_length=10, null=True, verbose_name='Zipcode')),
            ],
        ),
        migrations.AlterField(
            model_name='clientsurvey2024',
            name='zipcode',
            field=models.ForeignKey(blank=True, help_text='Please provide your zipcode', null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.zipcodesurvey', verbose_name='Zipcode'),
        ),
    ]