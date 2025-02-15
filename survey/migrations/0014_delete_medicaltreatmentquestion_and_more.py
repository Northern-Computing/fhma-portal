# Generated by Django 5.0.6 on 2024-11-24 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0013_clientsurvey2024_medical_treatment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MedicalTreatmentQuestion',
        ),
        migrations.AddField(
            model_name='clientsurvey2024',
            name='helped_leave_home',
            field=models.JSONField(default=list, help_text='Please select the appropriate options', verbose_name='Has having incontinent products helped you to leave home more to:'),
        ),
        migrations.AlterField(
            model_name='clientsurvey2024',
            name='other_comments',
            field=models.TextField(blank=True, help_text='Please provide any additional comments', null=True, verbose_name='Additional Comments (Other)'),
        ),
    ]
