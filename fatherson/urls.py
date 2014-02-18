from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
                       url(r'^$', views.show, name='formshow'),
                       url(r'calc/$', views.calc, name='calc'),
)