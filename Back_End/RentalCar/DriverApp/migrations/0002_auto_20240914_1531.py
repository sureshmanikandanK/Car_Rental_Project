# Generated by Django 3.2.19 on 2024-09-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DriverApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('license', models.CharField(max_length=50, unique=True)),
                ('vehicle_model', models.CharField(max_length=100)),
                ('vehicle_year', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='driver',
            name='phone',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]