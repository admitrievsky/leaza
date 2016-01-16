from article.models import Article
from django.utils.timezone import utc
import datetime


def run():
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    for a in Article.objects.only('pk', 'rating', 'created'):
        a.weight = a.rating - (now - a.created).total_seconds()/60/5
        a.save()
