# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('author_name', models.CharField(null=True, max_length=100, blank=True)),
                ('type', models.IntegerField(choices=[(1, 'Article'), (2, 'Comment')])),
                ('title', models.CharField(max_length=140)),
                ('slug', models.CharField(db_index=True, editable=False, max_length=400)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('comment_count', models.IntegerField(editable=False, default=0)),
                ('rating', models.IntegerField(editable=False, default=0)),
                ('weight', models.FloatField(editable=False, default=1000000)),
                ('author', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='')),
                ('article', models.ForeignKey(to='article.Article', related_name='images', editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleVote',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('mark', models.IntegerField()),
                ('article', models.ForeignKey(to='article.Article', related_name='votes', editable=False)),
                ('user', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentTree',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('position', models.TextField(max_length=200)),
                ('content', models.OneToOneField(to='article.Article', related_name='comment_tree_entry', editable=False)),
                ('parent', models.ForeignKey(to='article.Article', related_name='comment_children', editable=False)),
                ('root', models.ForeignKey(to='article.Article', related_name='comments', editable=False)),
            ],
        ),
    ]
