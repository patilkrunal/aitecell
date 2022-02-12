from django.contrib import admin
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
    OtherDetails,
)


admin.site.register(AllSections)
admin.site.register(Tag)
admin.site.register(Event)
admin.site.register(Update)
admin.site.register(Videos)
admin.site.register(Startup_Initiative)
admin.site.register(People)
admin.site.register(Links)
admin.site.register(Internships)
admin.site.register(Collaboration)
admin.site.register(OtherDetails)