# Generated by Django 4.1.3 on 2022-11-05 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dubai', '0019_alter_usermodel_salutation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='salutation',
        ),
    ]
