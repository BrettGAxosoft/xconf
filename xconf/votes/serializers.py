from mezzanine.accounts.models import User

from rest_framework import serializers
from rest_framework.fields import Field

from .models import Vote


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()
    voter = serializers.Field(source="user.username")

    class Meta:
        model = Vote
        fields = ('id', 'talk', 'voter')


class VoterSerialize(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()
    votes = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        field = ('id', 'username', 'votes')
