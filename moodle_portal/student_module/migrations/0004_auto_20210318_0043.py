# Generated by Django 3.1.5 on 2021-03-17 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_module', '0003_auto_20210317_2343'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='submission',
            unique_together=set(),
        ),
    ]
