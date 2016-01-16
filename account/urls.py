from django.conf.urls import url

from . import views
import django.contrib.auth.views

urlpatterns = [
    url(r'^u/(?P<slug>[^/]+)/$', views.display, name='display'),
    url(r'^$', views.display, name='display-current'),
    url(r'^edit/(?P<slug>[^/]+)/$', views.edit, name='edit'),
    url(r'^change-password/$',
        lambda x: django.contrib.auth.views.password_change(x,
                                             post_change_redirect='account:display-current',
                                             template_name='account/change-password.html'),
        name='change-password'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.RegistrationView.as_view(), name='register')
]
