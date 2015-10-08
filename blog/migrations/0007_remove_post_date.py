# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
    ]
