from .models import User, Corporation, Application
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'name', ]


class CorporationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Corporation
        fields = ['uid', 'name']

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Application
        fields = ['student', 'done_interview', 'resume','transcript']