# Generated by Django 3.1.5 on 2021-01-10 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Login', '0011_auto_20210110_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interviewer',
            fields=[
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=500, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=13)),
                ('company_name', models.CharField(max_length=1000)),
                ('position', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('admin_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.companyadmin')),
            ],
        ),
    ]
