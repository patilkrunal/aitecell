from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class EventType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    image_url = models.URLField(blank=True)
    meet_url = models.URLField(blank=True)
    event_type = models.ForeignKey(
        EventType, on_delete=models.CASCADE, default=1, related_name="events"
    )
    others = models.TextField(blank=True)
    files_attachment = models.FileField(upload_to="media/files/", blank=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Update(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def is_active(self):
        return self.date_from <= timezone.now() <= self.date_to


class Documents(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    document_link = models.URLField(blank=True)
    image = models.ImageField(upload_to="media/documents/", blank=True)

    class Meta:
        verbose_name_plural = "Documents"

    def __str__(self):
        return self.title


class Videos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    video_link = models.URLField()

    def __str__(self):
        return self.title


class Startup_Initiative(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="media/startup_initiative/", blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

def current_year():
    return datetime.date.today().year

class People(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="media/people/", blank=True)
    description = models.TextField(blank=True)
    social_links = models.TextField(blank=True)
    category = models.ManyToManyField(Category, blank=True)
    passout_year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])

    def __str__(self):
        return self.name


class Links(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    description = models.TextField(blank=True)
    logo_url = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "Links"

    def __str__(self):
        return self.title


class Internships(models.Model):
    title = models.CharField(max_length=100)
    company_link = models.URLField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="media/internships/", blank=True)
    apply_link = models.URLField(blank=True)
    deadline = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Internships"

    def __str__(self):
        return self.title


class Collaboration(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="media/collaboration/", blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title
