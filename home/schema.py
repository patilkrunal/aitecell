import graphene
from graphene_django import DjangoObjectType

from .models import (
    EventType,
    Event,
    Update,
    Documents,
    Videos,
    Startup_Initiative,
    Category,
    People,
    Links,
    Internships,
    Collaboration,
)


class EventTypeObjectType(DjangoObjectType):
    class Meta:
        model = EventType
        fields = "__all__"


class EventObjectType(DjangoObjectType):
    class Meta:
        model = Event
        fields = "__all__"


class UpdateType(DjangoObjectType):
    class Meta:
        model = Update
        fields = "__all__"


class DocumentsType(DjangoObjectType):
    class Meta:
        model = Documents
        fields = "__all__"


class VideosType(DjangoObjectType):
    class Meta:
        model = Videos
        fields = "__all__"


class Startup_InitiativeType(DjangoObjectType):
    class Meta:
        model = Startup_Initiative
        fields = "__all__"


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
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
    eventtypes = graphene.List(EventTypeObjectType)
    events = graphene.List(EventObjectType)
    latestupdates = graphene.List(UpdateType)
    documents = graphene.List(DocumentsType)
    videos = graphene.List(VideosType)
    startups = graphene.List(Startup_InitiativeType)
    categories = graphene.List(CategoryType)
    people = graphene.List(PeopleType)
    links = graphene.List(LinksType)
    internships = graphene.List(InternshipsType)
    collaboration = graphene.List(CollaborationType)

    def resolve_eventtypes(root, info, **kwargs):
        return EventType.objects.all()

    def resolve_events(root, info, **kwargs):
        return Event.objects.all()

    def resolve_latestupdates(root, info, **kwargs):
        return Update.objects.all()

    def resolve_documents(root, info, **kwargs):
        return Documents.objects.all()

    def resolve_videos(root, info, **kwargs):
        return Videos.objects.all()

    def resolve_startups(root, info, **kwargs):
        return Startup_Initiative.objects.all()

    def resolve_categories(root, info, **kwargs):
        return Category.objects.all()

    def resolve_people(root, info, **kwargs):
        return People.objects.all()

    def resolve_links(root, info, **kwargs):
        return Links.objects.all()

    def resolve_internships(root, info, **kwargs):
        return Internships.objects.all()

    def resolve_collaboration(root, info, **kwargs):
        return Collaboration.objects.all()


schema = graphene.Schema(query=Query)
