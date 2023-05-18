# Generated by Django 4.1.3 on 2023-04-03 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_student_notification_student_leave_student_feedback_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adminhod',
            options={'verbose_name': 'Teacher', 'verbose_name_plural': 'Teachers'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Teacher', 'verbose_name_plural': 'Teachers'},
        ),
        migrations.AddField(
            model_name='adminhod',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
