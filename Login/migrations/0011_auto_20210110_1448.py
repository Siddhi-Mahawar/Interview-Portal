# Generated by Django 3.1.5 on 2021-01-10 09:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0010_auto_20210110_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 10, 9, 28, 18, 668333, tzinfo=utc)),
        ),
    ]