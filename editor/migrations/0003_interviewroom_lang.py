# Generated by Django 3.1.5 on 2021-02-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0002_interviewroom_freeze'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewroom',
            name='lang',
            field=models.CharField(default='text/x-c++src', max_length=50),
        ),
    ]
