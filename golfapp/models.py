from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


# ____________________________________________________________Dashboard - Profile

SKILL_CHOICES = (
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
    ('Professional', 'Professional'),
)

INDEX_CHOICES = (
    ('30+', '30+'),
    ('20-29', '20-29'),
    ('10-19', '10-19'),
    ('Scratch-9', 'Scratch-9'),
)

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class UserInfo(models.Model):
    user = models.OneToOneField(User,related_name='info')
    buddies = models.ManyToManyField("self", blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30, blank=True)
    skill_level = models.CharField(max_length=50, choices=SKILL_CHOICES)
    handicap = models.CharField(max_length=50, choices=INDEX_CHOICES)
    birth_date = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    industry = models.CharField(max_length=30, blank=True)
    occupation = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=30, blank=True)
    website = models.URLField("Website", blank=True)
    photo = models.ImageField(upload_to='media', blank=True)

    def __unicode__(self):
        return self.name

# ____________________________________________________________Dashboard - Filter users


# ____________________________________________________________Dashboard - Tracker/Create Event


COURSE_CHOICES = (
    ('Harding Park', 'Harding Park'),
    ('Lincoln Park', 'Lincoln Park'),
    ('Sneath Lane', 'Sneath Lane'),
    ('Cypress Park', 'Cypress Park')
)



# ____________________________________________________________Dashboard - Invites



# ____________________________________________________________Dashboard - Activity Wall



# ____________________________________________________________Dashboard - Calendar

