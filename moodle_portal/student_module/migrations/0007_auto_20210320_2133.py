# Generated by Django 3.1.5 on 2021-03-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_module', '0006_submission_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='marks',
            field=models.FloatField(default=None, null=True),
        ),
    ]
