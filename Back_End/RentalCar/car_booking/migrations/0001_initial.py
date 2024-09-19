# Generated by Django 3.2.19 on 2024-09-12 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('booking_date', models.DateField()),
                ('pickup_date', models.DateField()),
                ('return_date', models.DateField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('canceled', 'Canceled')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('seat_type', models.CharField(max_length=50)),
                ('automatic', models.BooleanField(default=False)),
                ('gps', models.BooleanField(default=False)),
                ('speed', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('img_url', models.URLField()),
                ('car_name', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('brand', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cancellation',
            fields=[
                ('cancellation_id', models.AutoField(primary_key=True, serialize=False)),
                ('cancellation_date', models.DateField()),
                ('reason', models.TextField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_booking.booking')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='car_booking.car'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('availability_id', models.AutoField(primary_key=True, serialize=False)),
                ('pickup_date', models.DateField(blank=True, null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('available_quantity', models.IntegerField(null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_booking.car')),
            ],
            options={
                'unique_together': {('car', 'pickup_date', 'return_date')},
            },
        ),
    ]
