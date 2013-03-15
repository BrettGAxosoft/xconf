from mezzanine.blog.models import BlogPost

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from .serializers import TalkSerializer



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'talks': reverse('talk-list', request=request),
    })


class TalkList(generics.ListAPIView):
    model = BlogPost
    serializer_class = TalkSerializer
    paginate_by = 10


class TalkDetail(generics.RetrieveAPIView):
    model = BlogPost
    serializer_class = TalkSerializer

