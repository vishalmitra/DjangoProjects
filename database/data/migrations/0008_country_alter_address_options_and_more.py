# Generated by Django 4.1.7 on 2023-04-08 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_address_author_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('code', models.CharField(max_length=5)),
            ],
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address_of_the_author'},
        ),
        migrations.AddField(
            model_name='books',
            name='published_countries',
            field=models.ManyToManyField(to='data.country'),
        ),
    ]
