from rest_framework import viewsets, permissions
from .models import EventType, Event, Update, Documents, Videos, \
    Startup_Initiative, Category, People, Links, \
    Internships, Collaboration
from .serializers import \
    EventTypeSerializer, EventSerializer, UpdateSerializer, DocumentsSerializer, \
    VideosSerializer, StartupInitiativeSerializer, CategorySerializer, \
    PeopleSerializer, LinksSerializer, InternshipsSerializer, \
    CollaborationSerializer


class EventTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Basic Information to be created, viewed or modified
    """
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Basic Information to be created, viewed or modified
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UpdateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Projects to be created, viewed or modified.
    """
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DocumentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Experiences to be created, viewed or modified.
    """
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer
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
    queryset = Startup_Initiative.objects.all()
    serializer_class = StartupInitiativeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Links to be created, viewed or modified.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class PeopleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Links to be created, viewed or modified.
    """
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


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


class CollaborationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Links to be created, viewed or modified.
    """
    queryset = Collaboration.objects.all()
    serializer_class = CollaborationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


