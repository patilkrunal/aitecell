from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.db.models import Q
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
import datetime

from .models import (
    Event,
    Headline,
    Videos,
    StartupInitiative,
    People,
    Links,
    Internships,
    Collaboration,
)
from .serializers import (
    EventSerializer,
    UpdateSerializer,
    VideosSerializer,
    StartupInitiativeSerializer,
    PeopleSerializer,
    LinksSerializer,
    InternshipsSerializer,
    CollaborationSerializer,
)


def home(request):
    template = loader.get_template("home/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


class EventViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    Additionally we also provide an extra `upcoming_events`, `live_events`, `past_events` action.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=["get"])
    def upcoming_events(self, request, *args, **kwargs):
        upcoming_events = Event.objects.filter(
            Q(start_date__gte=datetime.datetime.now())
        ).order_by("-end_date")

        serializer = self.get_serializer(upcoming_events, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def live_events(self, request, *args, **kwargs):
        live_events = Event.objects.filter(
            Q(
                start_date__lte=datetime.datetime.now(),
                end_date__gte=datetime.datetime.now(),
            )
        ).order_by("-end_date")

        serializer = self.get_serializer(live_events, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def past_events(self, request, *args, **kwargs):
        past_events = Event.objects.filter(
            Q(end_date__lte=datetime.datetime.now())
        ).order_by("-end_date")

        serializer = self.get_serializer(past_events, many=True)
        return Response(serializer.data)


class UpdateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Projects to be created, viewed or modified.
    """

    queryset = Headline.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VideosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Education to be created, viewed or modified.
    """

    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StartupInitiativeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Skills to be created, viewed or modified.
    """

    queryset = StartupInitiative.objects.all()
    serializer_class = StartupInitiativeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PeopleViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    Additionally we also provide an extra `ecell_team` action.
    """

    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=["get"])
    def ecell_team(self, request, *args, **kwargs):
        ecell_team = People.objects.filter(
            (
                Q(category__title__startswith="Team")
                | Q(category__title__startswith="Faculty")
            )
            & (Q(passout_year__gte=datetime.date.today().year))
        )

        serializer = self.get_serializer(ecell_team, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def ecell_team_alumni(self, request, *args, **kwargs):
        ecell_team = People.objects.filter(
            (
                Q(category__title__startswith="Team")
                | Q(category__title__startswith="Faculty")
            )
            & (Q(passout_year__lt=datetime.date.today().year))
        )

        serializer = self.get_serializer(ecell_team, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def alumni_entrepreneur(self, request, *args, **kwargs):
        alumni_entrepreneur = People.objects.filter(
            Q(category__title__startswith="Alumni")
        )

        serializer = self.get_serializer(alumni_entrepreneur, many=True)
        return Response(serializer.data)


class LinksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Links to be created, viewed or modified.
    """

    queryset = Links.objects.all()
    serializer_class = LinksSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class InternshipsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Links to be created, viewed or modified.
    """

    queryset = Internships.objects.all()
    serializer_class = InternshipsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=["get"])
    def is_active(self, request, *args, **kwargs):
        is_active = Internships.objects.filter(
            Q(deadline__gte=datetime.datetime.now())
        ).order_by("-deadline")

        serializer = self.get_serializer(is_active, many=True)
        return Response(serializer.data)


class CollaborationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Links to be created, viewed or modified.
    """

    queryset = Collaboration.objects.all()
    serializer_class = CollaborationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
