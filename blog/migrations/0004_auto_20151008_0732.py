# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151007_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='todays',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(max_length=1, choices=[(b'C', b'Completed'), (b'I', b'InProgress'), (b'N', b'NotStarted')]),
        ),
    ]
