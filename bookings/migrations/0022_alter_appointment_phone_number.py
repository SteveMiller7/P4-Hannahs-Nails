# Generated by Django 3.2.13 on 2022-06-07 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0021_alter_appointment_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
    ]
