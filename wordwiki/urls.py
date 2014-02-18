from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wordwiki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^fatherson/', include('fatherson.urls', namespace="fatherson")),
    url(r'^pages/', include('pages.urls', namespace="pages")),
    url(r'^admin/', include(admin.site.urls)),
)
