# Generated by Django 5.0.2 on 2024-03-07 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0018_flightseatmanager_is_changed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightseatmanager',
            name='is_changed',
        ),
        migrations.RemoveField(
            model_name='flightseatmanager',
            name='remarks',
        ),
    ]
