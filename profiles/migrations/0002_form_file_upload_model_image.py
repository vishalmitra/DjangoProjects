# Generated by Django 4.2 on 2023-05-20 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form_file_upload',
            name='model_image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
