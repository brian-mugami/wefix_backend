# Generated by Django 4.1.3 on 2022-11-05 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dubai', '0020_remove_usermodel_salutation'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='salutation',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
