from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns('',
                       # ex: /pages/
                       url(r'^$', views.index, name='index'),
                       # ex: /pages/hank_manna
                       url(r'^(?P<pk>\w+)/$', views.detail, name='detail'),
)