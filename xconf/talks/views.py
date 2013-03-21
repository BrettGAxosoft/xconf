import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from mezzanine.blog.models import BlogPost, BlogCategory
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from rest_framework.response import Response

from .models import Vote
from .serializers import TalkSerializer, TalkDetailSerializer, PaginatedTalkSerializer, CategorySerializer, VoteSerializer, VoteTalkDetailSerializer


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


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


class TalkFullDetail(generics.RetrieveAPIView):
    model = BlogPost
    serializer_class = TalkDetailSerializer


class CategoryList(generics.ListAPIView):
    model = BlogCategory
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    model = BlogCategory
    serializer_class = CategorySerializer


@api_view(['GET'])
def category_talks(request, pk):
    queryset = BlogCategory.objects.get(pk=pk).blogposts.all()
    paginator = Paginator(queryset, 8)

    try:
        page = int(request.QUERY_PARAMS.get('page'))
        talks = paginator.page(page)
    except (ValueError, PageNotAnInteger, EmptyPage):
        page = random.randint(1, paginator.num_pages)
        talks = paginator.page(page)

    serializer_context = {'request': request, 'page': page}
    serializer = PaginatedTalkSerializer(talks,
                                         context=serializer_context)
    return Response(serializer.data)


class CategoryUserVotes(generics.ListAPIView):
    model=Vote
    serializer_class = VoteTalkDetailSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        category = BlogCategory.objects.filter(pk=pk)
        return self.request.user.votes.filter(talk__categories=category)


@permission_classes((IsOwner, ))
class VoteList(generics.ListCreateAPIView):
    model = Vote
    serializer_class = VoteSerializer

    def pre_save(self, obj):
        obj.user = self.request.user

    def get_queryset(self):
        return Vote.objects.filter(user=self.request.user)


@permission_classes((IsOwner, ))
class VoteDetail(generics.RetrieveAPIView):
    model = Vote
    serializer_class = VoteSerializer

    def pre_save(self, obj):
        obj.user = self.request.user
