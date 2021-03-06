# Generated by Django 3.2.13 on 2022-06-07 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0018_rename_doctor_technician'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='doctor',
            new_name='nail_tech',
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('nail_tech', 'date', 'timeslot')},
        ),
    ]
