# Generated by Django 3.2.13 on 2022-06-08 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0030_appointments_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='customer_name',
        ),
    ]
