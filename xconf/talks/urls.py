from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TalkList, TalkDetail, VoteList, VoteDetail

urlpatterns = patterns('xconf.talks.views',
    url(r'^$', 'api_root'),
    url(r'^talks/$', TalkList.as_view(), name='blogpost-list'),
    url(r'^talks/$', TalkList.as_view(), name='talk-list'),
    url(r'^talks/(?P<pk>\d+)/$', TalkDetail.as_view(), name='blogpost-detail'),
    url(r'^talks/(?P<pk>\d+)/$', TalkDetail.as_view(), name='talk-detail'),
    url(r'^votes/$', VoteList.as_view(), name='vote-list'),
    url(r'^votes/(?P<pk>\d+)/$', VoteDetail.as_view(), name='vote-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
