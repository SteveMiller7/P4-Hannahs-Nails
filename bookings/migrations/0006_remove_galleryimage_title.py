# Generated by Django 3.2.13 on 2022-05-31 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_galleryimage_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryimage',
            name='title',
        ),
    ]
