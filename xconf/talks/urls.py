from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TalkList, TalkDetail, VoteList, VoteDetail, CategoryList, CategoryDetail, CategoryTalks, CategoryUserVotes

urlpatterns = patterns('xconf.talks.views',
    url(r'^$', 'api_root'),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^talks/$', TalkList.as_view(), name='blogpost-list'),
    url(r'^talks/$', TalkList.as_view(), name='talk-list'),
    url(r'^talks/(?P<pk>\d+)/$', TalkDetail.as_view(), name='blogpost-detail'),
    url(r'^talks/(?P<pk>\d+)/$', TalkDetail.as_view(), name='talk-detail'),
    url(r'^votes/$', VoteList.as_view(), name='vote-list'),
    url(r'^votes/(?P<pk>\d+)/$', VoteDetail.as_view(), name='vote-detail'),
    url(r'^categories/$', CategoryList.as_view(), name='category-list'),
    url(r'^categories/(?P<pk>\d+)/$', CategoryDetail.as_view(), name='category-detail'),
    url(r'^categories/(?P<pk>\d+)/talks$', CategoryTalks.as_view(), name='category-talks'),
    url(r'^categories/(?P<pk>\d+)/uservotes$', CategoryUserVotes.as_view(), name='category-uservotes'),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
