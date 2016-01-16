from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext

from article.models import Article
from lib.listing import listing


def home(request):
    articles = listing(request, Article.objects.filter(type=Article.ARTICLE).order_by('-weight'))

    return render_to_response('home.html', {
        'articles': articles
    },
        context_instance=RequestContext(request))


def latest(request):
    articles = listing(request, Article.objects.filter(type=Article.ARTICLE).order_by('-created'))

    return render_to_response('home.html', {
        'articles': articles
    },
        context_instance=RequestContext(request))