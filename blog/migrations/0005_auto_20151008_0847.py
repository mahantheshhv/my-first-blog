# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151008_0732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='todays',
        ),
        migrations.AddField(
            model_name='post',
            name='Activities_in_progress',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='problems',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='todays_Accomplishment',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
