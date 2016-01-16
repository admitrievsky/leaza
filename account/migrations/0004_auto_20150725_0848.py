# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='slug',
            field=models.CharField(max_length=400, db_index=True),
        ),
    ]
