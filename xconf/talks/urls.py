from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TalkList, TalkDetail

urlpatterns = patterns('xconf.talks.views',
    url(r'^$', TalkList.as_view(), name='blogpost-list'),
    url(r'^(?P<pk>\d+)/$', TalkDetail.as_view(), name='blogpost-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
