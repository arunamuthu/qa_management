# Generated by Django 3.0.4 on 2020-05-17 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20200517_1032'),
        ('address', '0003_auto_20200503_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
        migrations.AddField(
            model_name='address',
            name='user_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.Profile'),
            preserve_default=False,
        ),
    ]
