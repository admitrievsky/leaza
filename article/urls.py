from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<slug>[^/]+)/$', views.edit, name='edit'),
    url(r'^a/(?P<slug>[^/]+)/$', views.full_view, name='full'),

    url(r'^vote/$', views.vote, name='vote'),
]