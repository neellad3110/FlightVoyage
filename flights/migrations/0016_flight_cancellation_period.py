# Generated by Django 5.0.2 on 2024-03-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0015_flightbookinglog_delete_userflightlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='cancellation_period',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
