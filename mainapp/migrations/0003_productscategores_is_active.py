# Generated by Django 3.1.4 on 2020-12-11 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='productscategores',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна'),
        ),
    ]
