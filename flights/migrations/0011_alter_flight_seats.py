# Generated by Django 5.0.2 on 2024-03-02 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0010_alter_bookinglog_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='seats',
            field=models.IntegerField(editable=False),
        ),
    ]
