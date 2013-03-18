from django.core.paginator import Paginator, PageNotAnInteger

from mezzanine.blog.models import BlogPost, BlogCategory
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from .models import Vote
from .serializers import TalkSerializer, CategorySerializer, VoteSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'talks': reverse('talk-list', request=request),
        'votes': reverse('vote-list', request=request),
        'categories': reverse('category-list', request=request),
    })


class TalkList(generics.ListAPIView):
    model = BlogPost
    serializer_class = TalkSerializer


class TalkDetail(generics.RetrieveAPIView):
    model = BlogPost
    serializer_class = TalkSerializer


class CategoryList(generics.ListAPIView):
    model = BlogCategory
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    model = BlogCategory
    serializer_class = CategorySerializer


class CategoryTalks(generics.ListAPIView):
    model = BlogPost
    serializer_class = TalkSerializer
    paginate_by = 8

    def get_queryset(self):
        pk = self.kwargs['pk']
        return BlogCategory.objects.get(pk=pk).blogposts.all()


class VoteList(generics.ListCreateAPIView):
    model = Vote
    serializer_class = VoteSerializer

    def pre_save(self, obj):
        obj.user = self.request.user


class VoteDetail(generics.RetrieveDestroyAPIView):
    model = Vote
    serializer_class = VoteSerializer

    def pre_save(self, obj):
        obj.user = self.request.user
