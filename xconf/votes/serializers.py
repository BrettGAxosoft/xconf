from mezzanine.accounts.models import User

from rest_framework import serializers
from rest_framework.fields import Field

from .models import Vote


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()
    username = serializers.Field(source="user.username")

    class Meta:
        model = Vote
        fields = ('id', 'talk', 'username')


class VoterSerialize(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()

    class Meta:
        model = User
        field = ('id', 'username')
