# Generated by Django 4.2 on 2023-05-20 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form_file_upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_file', models.FileField(upload_to='data')),
            ],
        ),
    ]
