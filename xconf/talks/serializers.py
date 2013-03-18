from django.core.exceptions import ValidationError

from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.accounts.models import User

from rest_framework import serializers

from .models import Vote


class TalkSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()
    votes = serializers.Field(source='vote_set.count')
    category = serializers.Field(source='categories.all')

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'votes', 'category', 'description')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()
    talks = TalkSerializer(many=True, source='blogposts')

    class Meta:
        model = BlogCategory
        fields = ('id', 'title', 'talks')


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()
    voter = serializers.Field(source="user.username")

    class Meta:
        model = Vote
        fields = ('id', 'talk', 'voter')

    def validate_voter(self, attr, value):
        user = self.context['request'].user
        talk = attr['talk']
        if user.votes.filter(talk=talk):
            msg = u"Already voted on this talk"
            raise ValidationError(msg)
        if user.votes.filter(talk__categories=talk.categories.all()).count() >= 3:
            msg = u"Only 3 votes per user per talk type"
            raise ValidationError(msg)
        return attr


class VoterSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()
    votes = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        field = ('id', 'username', 'votes')
