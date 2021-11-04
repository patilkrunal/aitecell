from django.contrib import admin
from .models import EventType, Event, Update, Documents, Videos, \
    Startup_Initiative, Category, People, Links, \
    Internships, Collaboration


admin.site.register(EventType)
admin.site.register(Event)
admin.site.register(Update)
admin.site.register(Documents)
admin.site.register(Videos)
admin.site.register(Startup_Initiative)
admin.site.register(Category)
admin.site.register(People)
admin.site.register(Links)
admin.site.register(Internships)
admin.site.register(Collaboration)
