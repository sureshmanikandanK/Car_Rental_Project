# Generated by Django 3.2.19 on 2024-09-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='img_url',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
