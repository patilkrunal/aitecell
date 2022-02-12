import datetime

from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.apps import apps


class AllSections(models.Model):
    section_name    = models.CharField(max_length=100)
    is_active       = models.BooleanField(default=False)

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
    title       = models.CharField(max_length=100)
    link        = models.URLField()
    description = models.TextField(blank=True)
    tag         = models.ForeignKey(Tag, on_delete=models.DO_NOTHING, related_name="links")
    logo_url    = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "Links"

    def __str__(self):
        return self.title


class Event(models.Model):
    title           = models.CharField(max_length=100)
    description     = RichTextField(config_name="awesome_ckeditor", null=True, blank=True)
    start_date      = models.DateTimeField(blank=True, null=True)
    end_date        = models.DateTimeField(blank=True, null=True)
    image_url       = models.URLField(blank=True)
    meet_url        = models.URLField(blank=True)
    event_type      = models.ForeignKey(Tag, on_delete=models.DO_NOTHING, related_name="events")
    tags            = models.ManyToManyField(Tag, related_name='event', default=None)
    documents_links = models.ManyToManyField(Links, related_name='event', default=None)
    others          = models.TextField(blank=True)
    comments        = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Update(models.Model):
    title       = models.CharField(max_length=100)
    link        = models.URLField(blank=True)
    start_date  = models.DateTimeField(default=timezone.now)
    end_date    = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def is_active(self):
        if self.start_date <= timezone.now() and self.end_date:
            return timezone.now() <= self.end_date
        else:
            return False

    def new_badge(self):
        def is_within_last_3_instance(self):
            latest_3_instances = Update.objects.all().order_by('-id')[:3]
            for instance in latest_3_instances:
                if instance.id == self.id:
                    return True
            return False

        return  self.is_active() and \
                self.start_date >= timezone.now() - datetime.timedelta(days=7) and \
                is_within_last_3_instance(self)


class Videos(models.Model):
    title       = models.CharField(max_length=100)
    video_link  = models.URLField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Startup_Initiative(models.Model):
    title           = models.CharField(max_length=100)
    description     = RichTextField(config_name="awesome_ckeditor", null=True, blank=True)
    image_link      = models.URLField(blank=True)
    document_link   = models.URLField(blank=True)
    website         = models.URLField(blank=True)

    def __str__(self):
        return self.title


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value) + 3


def current_year():
    return datetime.date.today().year


class People(models.Model):
    name            = models.CharField(max_length=100)
    designation     = models.CharField(max_length=200, blank=True)
    image_link      = models.URLField(blank=True)
    description     = RichTextField(config_name="awesome_ckeditor", null=True, blank=True)
    linkedin        = models.URLField(blank=True)
    instagram       = models.URLField(blank=True)
    tags            = models.ManyToManyField(Tag, related_name='people', default=None)
    is_active       = models.BooleanField(default=True)
    batch           = models.PositiveIntegerField(_("year"), blank=True, null=True,
                        validators=[MinValueValidator(1950), max_value_current_year],
                    )

    def __str__(self):
        return self.name


class Internships(models.Model):
    title           = models.CharField(max_length=100)
    company_link    = models.URLField(blank=True)
    description     = RichTextField(config_name="awesome_ckeditor", null=True, blank=True)
    image_link      = models.URLField(blank=True)
    apply_link      = models.URLField(blank=True)
    deadline        = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Internships"

    def __str__(self):
        return self.title


    def is_active(self):
        return self.deadline and self.deadline >= timezone.now()


class Collaboration(models.Model):
    title       = models.CharField(max_length=100)
    description = RichTextField(config_name="awesome_ckeditor", null=True, blank=True)
    image_link  = models.URLField(blank=True)
    website     = models.URLField(blank=True)

    def __str__(self):
        return self.title

class OtherDetails(models.Model):
    motto   = RichTextField(config_name="awesome_ckeditor", null=True, blank=True)
    vision  = RichTextField(config_name="awesome_ckeditor", null=True, blank=True)
    mission = RichTextField(config_name="awesome_ckeditor", null=True, blank=True)

    def __str__(self):
        return self.motto

    def save(self, *args, **kwargs):
        if OtherDetails.objects.exists() and not self.pk:
            raise ValidationError("Only one instance of this model is allowed.")
        return super().save(*args, **kwargs)