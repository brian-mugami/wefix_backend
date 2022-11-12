# Generated by Django 4.1.3 on 2022-11-04 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dubai', '0012_rename_worktype_worktypemodel_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='connectionmodel',
            old_name='worker_likes',
            new_name='likes',
        ),
        migrations.RenameField(
            model_name='workersmodel',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='seekersmodel',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dubai.usermodel'),
        ),
    ]