# Generated by Django 4.1.3 on 2022-11-05 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dubai', '0018_alter_usermodel_salutation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='salutation',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
