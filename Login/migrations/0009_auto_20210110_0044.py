# Generated by Django 3.1.5 on 2021-01-09 19:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0008_verification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 9, 19, 24, 51, 368240, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='verification',
            name='token',
            field=models.CharField(default='hey', max_length=200),
        ),
    ]
