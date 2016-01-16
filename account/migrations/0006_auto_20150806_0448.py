# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20150805_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='articles_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='comments_count',
            field=models.IntegerField(default=0),
        ),
    ]
