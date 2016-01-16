# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='article_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='comment_rating',
            field=models.IntegerField(default=0),
        ),
    ]
