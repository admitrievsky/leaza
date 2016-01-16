"""se URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import os

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include, url
from django.contrib import admin
from article import urls as article_urls
from account import urls as account_urls

from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url('', include('social.apps.django_app.urls', namespace='social')),


    url(r'^$', views.home, name='home'),
    url(r'^a/latest/', views.latest, name='latest'),
    url(r'^a/', include(article_urls, namespace='article')),
    url(r'^u/', include(account_urls, namespace='account')),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=os.path.join(settings.BASE_DIR, 'media'), show_indexes=True)

