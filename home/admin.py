from django.contrib import admin
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
    OtherDetails,
)


admin.site.register(AllSections)
admin.site.register(Tag)
admin.site.register(Event)
admin.site.register(Headline)
admin.site.register(Videos)
admin.site.register(StartupInitiative)
admin.site.register(People)
admin.site.register(Links)
admin.site.register(Internships)
admin.site.register(Collaboration)
admin.site.register(OtherDetails)