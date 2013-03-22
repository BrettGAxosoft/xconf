from django.core.exceptions import ValidationError
from django.template.defaultfilters import truncatewords_html

from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.accounts.models import User

from rest_framework import serializers, pagination

from .models import Vote


class TalkSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()
    votes = serializers.Field(source='vote_set.count')
    category = serializers.Field(source='categories.all')
    description = serializers.SerializerMethodField('get_descrption')

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'votes', 'category', 'description', 'speakers', 'office')

    def get_descrption(self, obj):
        return truncatewords_html(obj.content, 12)

class TalkDetailSerializer(TalkSerializer):
    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'votes', 'category', 'description', 'speakers', 'office')

    def get_descrption(self, obj):
        return obj.content


class PaginatedTalkSerializer(pagination.PaginationSerializer):
    page = serializers.SerializerMethodField('get_page')

    def get_page(self, obj):
        return self.context['page']

    class Meta:
        object_serializer_class = TalkSerializer


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()

    class Meta:
        model = BlogCategory
        fields = ('id', 'title')


class VoteSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    voter = serializers.Field(source="user.username")

    class Meta:
        model = Vote
        fields = ('id', 'talk', 'voter')

    def validate_voter(self, attr, value):
        raise ValidationError("Voting closed!!!!")
        user = self.context['request'].user
        talk = attr['talk']
        if user.votes.filter(talk=talk):
            msg = u"Already voted on this talk"
            raise ValidationError(msg)
        if user.votes.filter(talk__categories=talk.categories.all()).count() >= 10:
            msg = u"Only 10 votes per user per talk type"
            raise ValidationError(msg)
        return attr

class VoteTalkDetailSerializer(VoteSerializer):
    talk = TalkSerializer()

    class Meta:
        model = Vote
        fields = ('id', 'talk', 'voter')


class VoterSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()
    votes = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        field = ('id', 'username', 'votes')
