# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-11 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20180111_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='click_nums',
            field=models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570'),
        ),
    ]