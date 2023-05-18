# Generated by Django 4.1.3 on 2023-04-04 06:36

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_transport_manager_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=500)),
                ('book_code', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=500)),
                ('author_name', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('quantity', models.IntegerField(default=0)),
                ('code', models.ImageField(blank=True, upload_to='code')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.subjects')),
            ],
        ),
        migrations.CreateModel(
            name='Writer_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='IssuedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_code', models.CharField(max_length=788)),
                ('contact_number', models.CharField(max_length=788)),
                ('issued_date', models.DateField(auto_now_add=True)),
                ('expiry_date', models.DateField(default=app.models.expiry)),
                ('quantity', models.IntegerField(default=0, null=True)),
                ('book_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_nm', to='app.book_entry')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
        migrations.AddField(
            model_name='book_entry',
            name='writer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.writer_name'),
        ),
        migrations.CreateModel(
            name='Add_fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_category', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.course')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]