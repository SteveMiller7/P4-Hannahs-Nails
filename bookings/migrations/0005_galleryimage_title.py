# Generated by Django 3.2.13 on 2022-05-31 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_galleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='title',
            field=models.CharField(blank=True, max_length=40, unique=True),
        ),
    ]