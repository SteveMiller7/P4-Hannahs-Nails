# Generated by Django 3.2.13 on 2022-06-07 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0026_rename_appointment_appointments'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Required', max_length=20, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='appointments',
            unique_together={('nail_tech', 'date', 'timeslot', 'phone_number')},
        ),
    ]
