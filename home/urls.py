from django.urls import path, include
from rest_framework import routers

# from home import views
# urlpatterns = [
#     path('', views.home, name='home'),
# ]

from .views import EventViewSet, UpdateViewSet, DocumentsViewSet, VideosViewSet, \
    StartupInitiativeViewSet, CategoryViewSet, PeopleViewSet, LinksViewSet, \
    InternshipsViewSet, CollaborationViewSet


router = routers.DefaultRouter()

router.register(r'events', EventViewSet)
router.register(r'latestupdates', UpdateViewSet)
router.register(r'documents', DocumentsViewSet)
router.register(r'videos', VideosViewSet)
router.register(r'startups', StartupInitiativeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'people', PeopleViewSet)
router.register(r'links', LinksViewSet)
router.register(r'internships', InternshipsViewSet)
router.register(r'collaboration', CollaborationViewSet)

urlpatterns = router.urls

