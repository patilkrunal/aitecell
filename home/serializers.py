from abc import ABC

from rest_framework import serializers
from .models import EventType, Event, Update, Documents, Videos, \
    Startup_Initiative, Category, People, Links, \
    Internships, Collaboration


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ["__all__"]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["__all__"]


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = "__all__"


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = "__all__"


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = "__all__"


class StartupInitiativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup_Initiative
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = "__all__"


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = "__all__"


class InternshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internships
        fields = "__all__"


class CollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaboration
        fields = "__all__"

