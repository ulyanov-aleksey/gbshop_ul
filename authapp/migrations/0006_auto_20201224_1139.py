# Generated by Django 3.1.4 on 2020-12-24 08:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20201222_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuserprofile',
            name='photo',
            field=models.CharField(blank=True, max_length=128, verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 26, 8, 39, 26, 87431, tzinfo=utc)),
        ),
    ]
