# Generated by Django 2.2.11 on 2020-04-01 20:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_auto_20200401_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='todonode',
            name='percents_done',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
