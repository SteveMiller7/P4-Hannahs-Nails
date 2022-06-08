# Generated by Django 3.2.13 on 2022-06-08 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0027_auto_20220607_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='customer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='appointments',
            unique_together={('nail_tech', 'date', 'timeslot')},
        ),
    ]