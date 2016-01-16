# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20150707_0721'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='slug',
            field=models.CharField(editable=False, max_length=400, db_index=True, default='123'),
            preserve_default=False,
        ),
    ]
