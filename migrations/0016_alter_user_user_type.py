# Generated by Django 4.1.3 on 2023-04-04 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_book_entry_writer_name_issuedbook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('hod', 'HOD'), ('staff', 'STAFF'), ('student', 'STUDENT'), ('transport_manager', 'Transport Manager')], default=1, max_length=100),
        ),
    ]