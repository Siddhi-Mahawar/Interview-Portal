# Generated by Django 3.1.5 on 2021-01-09 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0006_auto_20210109_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyadmin',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
