# Generated by Django 4.1.3 on 2022-11-06 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dubai', '0022_remove_usermodel_salutation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 6, 19, 48, 23, 380408), max_length=100),
        ),
    ]
