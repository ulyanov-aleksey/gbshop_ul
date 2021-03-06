# Generated by Django 3.1.4 on 2020-12-24 08:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20201224_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 26, 8, 46, 42, 541289, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='photo',
            field=models.CharField(blank=True, max_length=128, verbose_name='фото из соц_сети'),
        ),
    ]
