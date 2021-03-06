# Generated by Django 3.1.5 on 2021-03-17 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_module', '0002_auto_20210317_1713'),
        ('login_module', '0002_auto_20210309_1723'),
        ('student_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('submission_id', models.AutoField(primary_key=True, serialize=False)),
                ('submission_file', models.FileField(null=True, upload_to='submissions/')),
                ('assignment', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='assignment', to='teacher_module.assignment')),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='assignment_student', to='login_module.student')),
            ],
        ),
    ]
