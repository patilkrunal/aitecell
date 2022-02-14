import datetime

from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.apps import apps
from django.db.models import Q


class AllSections(models.Model):
    section_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        if self.is_active:
            return self.section_name + ' (Active)'
        else:
            return self.section_name + ' (Inactive)'

    class Meta:
        verbose_name_plural = "AllSections"


class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        if self.title.count(" ") > 0:
            raise ValidationError(
                _("Tag must be single word. Please try again.")
            )

        if len(self.title) < 3:
            raise ValidationError(
                _("Tag must be at least 3 characters. Please try again.")
            )

        if self.pk is None:
            if Tag.objects.filter(title=self.title).exists():
                raise ValidationError(
                    _("Tag already exists. Please try again.")
                )

    def save(self, *args, **kwargs):
        self.clean_fields()
        self.title = self.title.lower()
        super().save(*args, **kwargs)


class Links(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    description = models.TextField(blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING,
                            related_name="links", null=True, blank=True)
    logo_url = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "Links"

    def __str__(self):
        return self.title


class Events(models.Manager):
    def get_queryset(self):
        return super(Events, self).get_queryset().filter(event_type__title="eventtype_event").order_by('-start_date')


class Visits(models.Manager):
    def get_queryset(self):
        return super(Visits, self).get_queryset().filter(event_type__title="eventtype_visit").order_by('-start_date')


class Sessions(models.Manager):
    def get_queryset(self):
        return super(Sessions, self).get_queryset().filter(event_type__title="eventtype_session").order_by('-start_date')


class Trainings(models.Manager):
    def get_queryset(self):
        return super(Trainings, self).get_queryset().filter(event_type__title="eventtype_training").order_by('-start_date')


class Event(models.Model):
    def limit_event_type_choices():
        return Q(title__startswith="eventtype_")

    def limit_tags_choices():
        return Q(title__startswith="event_")

    title = models.CharField(max_length=100)
    description = RichTextField(
        config_name="awesome_ckeditor", null=True, blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    image_url = models.URLField(blank=True)
    meet_url = models.URLField(blank=True)
    event_type = models.ForeignKey(Tag, limit_choices_to=limit_event_type_choices,
                                   on_delete=models.DO_NOTHING, related_name="events", null=True, blank=True)
    tags = models.ManyToManyField(
        Tag, limit_choices_to=limit_tags_choices, related_name='event', null=True, blank=True)
    documents_links = models.ManyToManyField(
        Links, related_name='event', null=True, blank=True)
    others = models.TextField(blank=True)
    comments = models.TextField(blank=True)

    objects = models.Manager()
    events = Events()
    visits = Visits()
    sessions = Sessions()
    trainings = Trainings()

    def __str__(self):
        return self.title


class UpdateManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(start_date__gte=(timezone.now() - datetime.timedelta(days=7))) | super().get_queryset().order_by('-id')[:3]


class Update(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()
    active_objects = UpdateManager()

    def __str__(self):
        return self.title


class Videos(models.Model):
    title = models.CharField(max_length=100)
    video_link = models.URLField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Startup_Initiative(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(
        config_name="awesome_ckeditor", null=True, blank=True)
    image_link = models.URLField(blank=True)
    document_link = models.URLField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.title


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year()+4)(value)


class TeamMember(models.Manager):
    def get_queryset(self):
        return super(TeamMember, self).get_queryset().filter(tags__title="people_team-member")


class AlumniEntrepreneurs(models.Manager):
    def get_queryset(self):
        return super(AlumniEntrepreneurs, self).get_queryset().filter(tags__title="people_alumni-entrepreneur")


class IndustrialMentors(models.Manager):
    def get_queryset(self):
        return super(IndustrialMentors, self).get_queryset().filter(tags__title="people_industrial-mentor")


class FacultyMentors(models.Manager):
    def get_queryset(self):
        return super(FacultyMentors, self).get_queryset().filter(tags__title="people_faculty-mentor")


class People(models.Model):
    def limit_tags_choices():
        return Q(title__startswith="people_")

    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=200, blank=True)
    image_link = models.URLField(blank=True)
    description = RichTextField(
        config_name="awesome_ckeditor", null=True, blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    tags = models.ManyToManyField(
        Tag, limit_choices_to=limit_tags_choices, related_name='people', default=None)
    is_active = models.BooleanField(default=True)
    batch = models.PositiveIntegerField(_("year"), null=True, blank=True,
                                        validators=[MinValueValidator(1998), max_value_current_year])

    objects = models.Manager()
    team_members = TeamMember()
    alumni_entrepreneurs = AlumniEntrepreneurs()
    industrial_mentors = IndustrialMentors()
    faculty_mentors = FacultyMentors()

    def __str__(self):
        return self.name


class Internships(models.Model):
    title = models.CharField(max_length=100)
    company_link = models.URLField(blank=True)
    description = RichTextField(
        config_name="awesome_ckeditor", null=True, blank=True)
    image_link = models.URLField(blank=True)
    apply_link = models.URLField(blank=True)
    deadline = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Internships"

    def __str__(self):
        return self.title

    def is_active(self):
        return self.deadline and self.deadline >= timezone.now()


class Collaboration(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(
        config_name="awesome_ckeditor", null=True, blank=True)
    image_link = models.URLField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.title


class OtherDetails(models.Model):
    motto = RichTextField(config_name="awesome_ckeditor",
                          null=True, blank=True)
    vision = RichTextField(
        config_name="awesome_ckeditor", null=True, blank=True)
    mission = RichTextField(
        config_name="awesome_ckeditor", null=True, blank=True)
    policy = RichTextField(
        config_name="awesome_ckeditor", null=True, blank=True)
    Rules = RichTextField(config_name="awesome_ckeditor",
                          null=True, blank=True)
    about_us = RichTextField(
        config_name="awesome_ckeditor", null=True, blank=True)

    def __str__(self):
        return self.motto

    def save(self, *args, **kwargs):
        if OtherDetails.objects.exists() and not self.pk:
            raise ValidationError(
                "Only one instance of this model is allowed.")
        return super().save(*args, **kwargs)
