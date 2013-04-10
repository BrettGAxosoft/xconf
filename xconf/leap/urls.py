from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('xconf.leap.views',
    url(r'^$', 'index'),
)

urlpatterns += staticfiles_urlpatterns()
