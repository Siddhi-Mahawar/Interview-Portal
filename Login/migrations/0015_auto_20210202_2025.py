# Generated by Django 3.1.5 on 2021-02-02 14:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0014_auto_20210111_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordrequest',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 2, 15, 5, 58, 717123, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='verification',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 2, 15, 5, 58, 717123, tzinfo=utc)),
        ),
    ]
