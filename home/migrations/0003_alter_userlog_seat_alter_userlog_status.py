# Generated by Django 5.0.2 on 2024-03-04 16:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_userlog_cancellation_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='seat',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='userlog',
            name='status',
            field=models.IntegerField(choices=[(-1, 'Cancelled'), (1, 'Confirmed')], default=0),
        ),
    ]