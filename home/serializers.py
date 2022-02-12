from rest_framework import serializers
from .models import (
    AllSections,
    Tag,
    Event,
    Update,
    Videos,
    Startup_Initiative,
    People,
    Links,
    Internships,
    Collaboration,
)


class AllSectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllSections
        fields = "__all__"


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    event_type = serializers.CharField(source="event_type.title")

    class Meta:
        model = Event
        fields = "__all__"


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = "__all__"


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = "__all__"


class StartupInitiativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup_Initiative
        fields = "__all__"


class PeopleSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True, read_only=True)

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
