# Generated by Django 3.1.5 on 2021-03-20 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_module', '0005_submission_submission_added_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='marks',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]