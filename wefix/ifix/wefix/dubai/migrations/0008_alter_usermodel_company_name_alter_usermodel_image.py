# Generated by Django 4.1.3 on 2022-11-04 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dubai', '0007_rename_company_name_usermodel_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='company_name',
            field=models.CharField(max_length=200, verbose_name='Company name(If Company)'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='image',
            field=models.CharField(max_length=200, verbose_name='Profile picture'),
        ),
    ]
