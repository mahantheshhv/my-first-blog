# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(max_length=1, choices=[(b'C', b'Completed'), (b'IP', b'In_Progress'), (b'NS', b'Not_Started')]),
        ),
    ]
