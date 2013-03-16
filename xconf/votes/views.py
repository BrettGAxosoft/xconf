from .models import Vote
from .serializers import VoteSerializer

from django.shortcuts import get_object_or_404

from mezzanine.utils.views import render

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'votes': reverse('vote-list', request=request),
    })


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