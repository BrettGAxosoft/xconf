from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import VoteList, VoteDetail

urlpatterns = patterns('xconf.votes.views',
    url(r'^$', VoteList.as_view(), name='vote-list'),
    url(r'^(?P<pk>\d+)/$', VoteDetail.as_view(), name='vote-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
