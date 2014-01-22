from django import forms
from django.contrib.auth.models import User
from golfapp.models import UserInfo
from django.core.validators import MaxLengthValidator
from django.forms.extras.widgets import SelectDateWidget


# ____________________________________________________________Signup

class UserForm(forms.ModelForm):
    class Meta(object):
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "username":forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            "email":forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'form-control'}),
            "password":forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
        }


class SignupForm(UserForm):
    confirm_password=forms.CharField(required=True,
        widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'})
    )


# ____________________________________________________________Login

class LoginForm(UserForm):
    class Meta(object):
        model = User
        fields = ["username", "password"]
        widgets = {
            "username":forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            "password":forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
        }


# ____________________________________________________________Dashboard - Profile

SKILL_CHOICES = (
    ('Beginner - 30+ handicap', 'Beginner - 30+ handicap'),
    ('Intermediate - 20-29 handicap', 'Intermediate - 20-29 handicap'),
    ('Advanced - 10-19 handicap', 'Advanced - 10-19 handicap'),
    ('Professional - Scrtch - 9 handicap', 'Professional - Scrtch - 9 handicap'),
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

class UserInfoForm(forms.ModelForm):
    class Meta(object):
        model = UserInfo
        fields = ['first_name', 'last_name', 'location', 'birth_date', 'skill_level', 'handicap', 'website', 'gender', 'industry', 'company', 'occupation', 'photo']
        widgets = {
            "first_name":forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            "last_name":forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            "location":forms.TextInput(attrs={'placeholder': 'City, State', 'class': 'form-control'}),
            "skill_level":forms.Select(choices=SKILL_CHOICES),
            "handicap":forms.Select(choices=INDEX_CHOICES),
            "birth_date":forms.DateInput(attrs={'placeholder': 'Birthday', 'class': 'form-control', 'type':"date", 'id':"dateForm"}),
            "gender":forms.Select(choices=GENDER_CHOICES),
            "industry":forms.TextInput(attrs={'placeholder': 'Industry', 'class': 'form-control'}),
            "company":forms.TextInput(attrs={'placeholder': 'Company', 'class': 'form-control'}),
            "occupation":forms.TextInput(attrs={'placeholder': 'Occupation', 'class': 'form-control'}),
            "website":forms.TextInput(attrs={'placeholder': 'Website URL', 'class': 'form-control'}),
        }
        
 
# ____________________________________________________________Dashboard - Activity Wall



# ____________________________________________________________Dashboard - Events - Create Event



# ____________________________________________________________Dashboard - Events - Course


# ____________________________________________________________Dashboard - Tracker - Scorecard

# class Course_ScoreForm(CoursesForm):
#     class Meta(object):
#         model = Course_Score
#         fields = ['hole_01', 'hole_02', 'hole_03', 'hole_04', 'hole_05', 'hole_06', 'hole_07', 'hole_08', 'hole_09', 'hole_10', 'hole_11', 'hole_12', 'hole_13', 'hole_14', 'hole_15', 'hole_16', 'hole_17', 'hole_18']
#         widgets = {
#             "hole_01":forms.NumberInput(attrs={'placeholder': '1'}),
#             "hole_02":forms.NumberInput(attrs={'placeholder': '2'}),
#             "hole_03":forms.NumberInput(attrs={'placeholder': '3'}),
#             "hole_04":forms.NumberInput(attrs={'placeholder': '4'}),
#             "hole_05":forms.NumberInput(attrs={'placeholder': '5'}),
#             "hole_06":forms.NumberInput(attrs={'placeholder': '6'}),
#             "hole_07":forms.NumberInput(attrs={'placeholder': '7'}),
#             "hole_08":forms.NumberInput(attrs={'placeholder': '8'}),
#             "hole_09":forms.NumberInput(attrs={'placeholder': '9'}),
#             "hole_10":forms.NumberInput(attrs={'placeholder': '10'}),
#             "hole_11":forms.NumberInput(attrs={'placeholder': '11'}),
#             "hole_12":forms.NumberInput(attrs={'placeholder': '12'}),
#             "hole_13":forms.NumberInput(attrs={'placeholder': '13'}),
#             "hole_14":forms.NumberInput(attrs={'placeholder': '14'}),
#             "hole_15":forms.NumberInput(attrs={'placeholder': '15'}),
#             "hole_16":forms.NumberInput(attrs={'placeholder': '16'}),
#             "hole_17":forms.NumberInput(attrs={'placeholder': '17'}),
#             "hole_18":forms.NumberInput(attrs={'placeholder': '18'}),
#         }


# ____________________________________________________________Dashboard - Create Event

COURSE_CHOICES = (
    ('Harding Park', 'Harding Park'),
    ('Lincoln Park', 'Lincoln Park'),
    ('Sneath Lane', 'Sneath Lane'),
    ('Cypress Park', 'Cypress Park')
)

# class EventForm(forms.ModelForm):
#     class Meta(object):
#         model = Event
#         fields = ["date", "course", "time"]
#         widgets = {
#             "date":forms.DateInput(attrs={'placeholder': 'Date', 'class': 'form-control', 'type':"date", 'id':"dateForm"}),
#             "course":forms.Select(choices=COURSE_CHOICES),
#             "time":forms.DateInput(attrs={'placeholder': 'Date', 'class': 'form-control', 'type':"time", 'id':"dateForm"})
#         }

