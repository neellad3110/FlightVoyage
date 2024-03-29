# Generated by Django 5.0.2 on 2024-03-02 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0012_alter_flight_seats_flightseatmanager_userflightlog_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightseatmanager',
            name='status',
            field=models.IntegerField(choices=[(-1, 'Cancelled'), (0, 'Pending'), (1, 'Confirmed')], default=0),
        ),
    ]
