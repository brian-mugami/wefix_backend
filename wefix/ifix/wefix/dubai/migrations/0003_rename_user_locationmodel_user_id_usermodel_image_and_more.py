# Generated by Django 4.1.3 on 2022-11-02 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dubai', '0002_remove_usermodel_username_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locationmodel',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='image',
            field=models.CharField(blank=True, max_length=200, verbose_name='Profile picture'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='Company_name',
            field=models.CharField(blank=True, max_length=200, unique=True, verbose_name='Company name(If Company)'),
        ),
        migrations.AlterField(
            model_name='workersmodel',
            name='Charge_type',
            field=models.CharField(choices=[('PER_HOUR', 'PER_HOUR'), ('PER_DAY', 'PER_DAY'), ('PER_MONTH', 'PER_MONTH'), ('PER_YEAR', 'PER_YEAR')], default='PER_DAY', max_length=20, verbose_name='Charge type'),
        ),
        migrations.AlterField(
            model_name='workersmodel',
            name='Experience',
            field=models.CharField(choices=[('< 1 YEAR', '< 1 YEAR'), ('> 1 YEAR', '> 1 YEAR'), ('3 YEARS +', '3 YEARS +')], default='< 1 YEAR', max_length=30, verbose_name='Experience'),
        ),
    ]
