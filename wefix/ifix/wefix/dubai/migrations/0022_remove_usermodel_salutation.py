# Generated by Django 4.1.3 on 2022-11-05 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dubai', '0021_usermodel_salutation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='salutation',
        ),
    ]
