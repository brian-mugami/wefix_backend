# Generated by Django 4.1.3 on 2022-11-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dubai', '0004_remove_locationmodel_user_id_usermodel_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationmodel',
            name='name',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
