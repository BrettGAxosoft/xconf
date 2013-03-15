from mezzanine.blog.models import BlogPost
from rest_framework import serializers
from rest_framework.fields import Field


class TalkSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()
    votes = serializers.Field(source='vote_set.count')

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'votes')
