import graphene
from graphene_django import DjangoObjectType

from .models import (
    AllSections,
    Tag,
    Event,
    Headline,
    Videos,
    StartupInitiative,
    People,
    Links,
    Internships,
    Collaboration,
    OtherDetails
)


class AllSectionsType(DjangoObjectType):
    class Meta:
        model = AllSections
        fields = "__all__"


class EventObjectType(DjangoObjectType):
    class Meta:
        model = Event
        fields = "__all__"


class HeadlineType(DjangoObjectType):
    class Meta:
        model = Headline
        fields = "__all__"


class VideosType(DjangoObjectType):
    class Meta:
        model = Videos
        fields = "__all__"


class Startup_InitiativeType(DjangoObjectType):
    class Meta:
        model = StartupInitiative
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


class OtherDetailsType(DjangoObjectType):
    class Meta:
        model = OtherDetails
        fields = "__all__"


class Query(graphene.ObjectType):
    allsectionstypes = graphene.List(AllSectionsType)
    events = graphene.List(EventObjectType)
    visits = graphene.List(EventObjectType)
    sessions = graphene.List(EventObjectType)
    trainings = graphene.List(EventObjectType)
    latestheadlines = graphene.List(HeadlineType)
    videos = graphene.List(VideosType)
    startups = graphene.List(Startup_InitiativeType)
    tags = graphene.List(TagType)
    people = graphene.List(PeopleType)
    teamMembers = graphene.List(PeopleType)
    alumniEntrepreneurs = graphene.List(PeopleType)
    industrialMentors = graphene.List(PeopleType)
    facultyMentors = graphene.List(PeopleType)
    links = graphene.List(LinksType)
    internships = graphene.List(InternshipsType)
    collaboration = graphene.List(CollaborationType)
    otherdetails = graphene.List(OtherDetailsType)

    def resolve_allsectionstypes(root, info, **kwargs):
        return AllSections.objects.all()

    def resolve_events(root, info, **kwargs):
        return Event.events.all()

    def resolve_visits(root, info, **kwargs):
        return Event.visits.all()

    def resolve_sessions(root, info, **kwargs):
        return Event.sessions.all()

    def resolve_trainings(root, info, **kwargs):
        return Event.trainings.all()

    def resolve_latestheadlines(root, info, **kwargs):
        return Headline.active_objects.all()

    def resolve_videos(root, info, **kwargs):
        return Videos.objects.all()

    def resolve_startups(root, info, **kwargs):
        return StartupInitiative.objects.all()

    def resolve_tags(root, info, **kwargs):
        return Tag.objects.all()

    def resolve_people(root, info, **kwargs):
        return People.objects.all()

    def resolve_teamMembers(root, info, **kwargs):
        return People.team_members.all()

    def resolve_alumniEntrepreneurs(root, info, **kwargs):
        return People.alumni_entrepreneurs.all()

    def resolve_industrialMentors(root, info, **kwargs):
        return People.industrial_mentors.all()

    def resolve_facultyMentors(root, info, **kwargs):
        return People.faculty_mentors.all()

    def resolve_links(root, info, **kwargs):
        return Links.objects.all()

    def resolve_internships(root, info, **kwargs):
        return Internships.objects.all()

    def resolve_collaboration(root, info, **kwargs):
        return Collaboration.objects.all()

    def resolve_otherdetails(root, info, **kwargs):
        return OtherDetails.objects.all()


schema = graphene.Schema(query=Query)
