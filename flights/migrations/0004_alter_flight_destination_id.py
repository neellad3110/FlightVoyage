# Generated by Django 5.0.2 on 2024-02-28 04:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_alter_flight_destination_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='destination_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_flights', to='flights.country'),
        ),
    ]
