# Generated by Django 3.2.13 on 2022-06-07 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0020_auto_20220607_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]