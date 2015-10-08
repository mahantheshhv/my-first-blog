# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(default=0, max_length=1, choices=[(b'C', b'Completed'), (b'IP', b'In Progress'), (b'NS', b'Not Started')]),
            preserve_default=False,
        ),
    ]
