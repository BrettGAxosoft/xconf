from mezzanine.blog.models import BlogPost
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from .models import Vote
from .serializers import TalkSerializer
from .serializers import VoteSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'talks': reverse('talk-list', request=request),
        'votes': reverse('vote-list', request=request)
    })


class TalkList(generics.ListAPIView):
    model = BlogPost
    serializer_class = TalkSerializer
    paginate_by = 10


class TalkDetail(generics.RetrieveAPIView):
    model = BlogPost
    serializer_class = TalkSerializer


class VoteList(generics.ListCreateAPIView):
    model = Vote
    serializer_class = VoteSerializer
    paginate_by = 10

    def pre_save(self, obj):
        obj.user = self.request.user


class VoteDetail(generics.RetrieveDestroyAPIView):
    model = Vote
    serializer_class = VoteSerializer

    def pre_save(self, obj):
        obj.user = self.request.user
