import graphene
from graphene_django import DjangoObjectType

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


class AllSectionsType(DjangoObjectType):
    class Meta:
        model = AllSections
        fields = "__all__"


class EventObjectType(DjangoObjectType):
    class Meta:
        model = Event
        fields = "__all__"


class UpdateType(DjangoObjectType):
    class Meta:
        model = Update
        fields = "__all__"


class VideosType(DjangoObjectType):
    class Meta:
        model = Videos
        fields = "__all__"


class Startup_InitiativeType(DjangoObjectType):
    class Meta:
        model = Startup_Initiative
        fields = "__all__"


class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = "__all__"


class PeopleType(DjangoObjectType):
    class Meta:
        model = People
        fields = "__all__"


class LinksType(DjangoObjectType):
    class Meta:
        model = Links
        fields = "__all__"


class InternshipsType(DjangoObjectType):
    class Meta:
        model = Internships
        fields = "__all__"


class CollaborationType(DjangoObjectType):
    class Meta:
        model = Collaboration
        fields = "__all__"


class Query(graphene.ObjectType):
    allsectionstypes = graphene.List(AllSectionsType)
    events = graphene.List(EventObjectType)
    latestupdates = graphene.List(UpdateType)
    videos = graphene.List(VideosType)
    startups = graphene.List(Startup_InitiativeType)
    categories = graphene.List(TagType)
    people = graphene.List(PeopleType)
    links = graphene.List(LinksType)
    internships = graphene.List(InternshipsType)
    collaboration = graphene.List(CollaborationType)

    def resolve_allsectionstypes(root, info, **kwargs):
        return AllSections.objects.all()

    def resolve_events(root, info, **kwargs):
        return Event.objects.all()

    def resolve_latestupdates(root, info, **kwargs):
        return Update.objects.all()

    def resolve_videos(root, info, **kwargs):
        return Videos.objects.all()

    def resolve_startups(root, info, **kwargs):
        return Startup_Initiative.objects.all()

    def resolve_categories(root, info, **kwargs):
        return Tag.objects.all()

    def resolve_people(root, info, **kwargs):
        return People.objects.all()

    def resolve_links(root, info, **kwargs):
        return Links.objects.all()

    def resolve_internships(root, info, **kwargs):
        return Internships.objects.all()

    def resolve_collaboration(root, info, **kwargs):
        return Collaboration.objects.all()


schema = graphene.Schema(query=Query)
