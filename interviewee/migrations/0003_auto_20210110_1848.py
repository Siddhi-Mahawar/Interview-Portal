# Generated by Django 3.1.5 on 2021-01-10 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviewee', '0002_auto_20210110_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewee',
            name='name',
            field=models.CharField(default='', max_length=250),
        ),
    ]