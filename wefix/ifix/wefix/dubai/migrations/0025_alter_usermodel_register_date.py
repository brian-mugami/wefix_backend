# Generated by Django 4.1.3 on 2022-11-06 19:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dubai', '0024_alter_usermodel_register_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='register_date',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=100),
        ),
    ]
