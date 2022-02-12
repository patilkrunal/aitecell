from rest_framework import routers

from .views import (
    EventViewSet,
    UpdateViewSet,
    VideosViewSet,
    StartupInitiativeViewSet,
    PeopleViewSet,
    LinksViewSet,
    InternshipsViewSet,
    CollaborationViewSet,
)


router = routers.DefaultRouter()

router.register(r"events", EventViewSet)
router.register(r"latestupdates", UpdateViewSet)
router.register(r"videos", VideosViewSet)
router.register(r"startups", StartupInitiativeViewSet)
router.register(r"people", PeopleViewSet)
router.register(r"links", LinksViewSet)
router.register(r"internships", InternshipsViewSet)
router.register(r"collaboration", CollaborationViewSet)

urlpatterns = router.urls
