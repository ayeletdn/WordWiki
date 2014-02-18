from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^new/$', views.new, name='new'),
                       url(r'^(?P<word>.+?)/$', views.detail, name='detail'),
)