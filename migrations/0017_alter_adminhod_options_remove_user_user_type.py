# Generated by Django 4.1.3 on 2023-04-04 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adminhod',
            options={'verbose_name': 'AdminHOD', 'verbose_name_plural': 'AdminHODS'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
    ]
