# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import account.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20150923_1728'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('objects', account.models.AccountManager()),
            ],
        ),
    ]
