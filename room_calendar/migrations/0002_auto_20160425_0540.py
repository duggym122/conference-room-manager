# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-25 05:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('room_calendar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reservation_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 25, 5, 55, 6, 106538, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_start',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 25, 5, 40, 6, 106475, tzinfo=utc)),
        ),
    ]
