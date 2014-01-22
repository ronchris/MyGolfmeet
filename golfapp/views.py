from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth.models import User
from golfapp.forms import UserForm, SignupForm, LoginForm, UserInfoForm
from golfapp.models import UserInfo
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from golfapp.models import *
import datetime

# ____________________________________________________________Home

def home_view(request):
        return render_to_response('home.html')

# ____________________________________________________________Signup

def signup_view(request):
    if request.method == "POST":
        print request.POST
        form = SignupForm(request.POST)
        print "Here"
        if form.is_valid():
            print "Valid"
            user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"],
            )
        print "There"
        return HttpResponseRedirect("/thanks/")
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/thanks/')
        else:
            # Show an error page
            data =  {
                "UserForm" : UserForm(),
                "SignupForm" : SignupForm()
            }
            return render(request, 'signup-page.html', data)

# ____________________________________________________________Login

@csrf_protect
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            return HttpResponseRedirect('/incorrect/')
    else:
        form = LoginForm()
        return render(request, 'login-page.html', {"LoginForm":form})


def incorrect_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect ('/dashboard/')
        else:
            return HttpResponseRedirect('/incorrect/')
    else:
        form = LoginForm()
        return render(request, 'incorrect-page.html', {"LoginForm":form})

# ____________________________________________________________Thanks

def show_thanks(request):
    return render_to_response('thanks.html')

# ____________________________________________________________Logout

@login_required
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

# ____________________________________________________________Dashboard

def show_dashboard(request):
    users = User.objects.all() # Display all users
    # users = User.objects.filter(info__skill_level__icontains="beginner").all() # Display all users
    user_count = User.objects.count() # Display total users
    dashboard_user = request.user # Display the loggedin user
    print dashboard_user # See name of loggedin user in terminal


    # if request.method == 'GET':
    #     form = EventForm()
    # else:
    #     # A POST request: Handle Form Upload
    #     form = EventForm(request.POST) # Bind data from request.POST into a PostForm

    #     # If data is valid, proceeds to create new profile post and redirect the user
    #     if form.is_valid():

    #         event = Event()

    #         event.user_id = request.user.id
    #         event.date = form.cleaned_data['date']
    #         event.location= form.cleaned_data['location']
    #         event.time = form.cleaned_data['time']
            
    #         event.save()
    #         return HttpResponseRedirect('/dashboard/')

    # events = Event.objects.all()

    return render(request, 'dashboard.html', {'users':users, 'dashboard_user':dashboard_user, 'user_count':user_count})

# ____________________________________________________________Dashboard - Profile

@login_required
def create_profile(request):
    if request.method == 'GET':
        form = UserInfoForm()
    else:
        # A POST request: Handle Form Upload
        form = UserInfoForm(request.POST) # Bind data from request.POST into a PostForm

        # If data is valid, proceeds to create new profile post and redirect the user
        if form.is_valid():

            info = UserInfo()

            info.user_id = request.user.id
            info.first_name = form.cleaned_data['first_name']
            info.last_name = form.cleaned_data['last_name']
            info.location= form.cleaned_data['location']
            info.skill_level = form.cleaned_data['skill_level']
            info.handicap = form.cleaned_data['handicap']
            info.birth_date = form.cleaned_data['birth_date']
            info.gender = form.cleaned_data['gender']
            info.industry = form.cleaned_data['industry']
            info.company = form.cleaned_data['company']
            info.occupation = form.cleaned_data['occupation']
            info.website = form.cleaned_data['website']

            info.save()
            return HttpResponseRedirect('dashboard/profile/profile_view/')

    return render(request, 'profile.html', {'form': form})


def view_profile(request):
    return render(request, 'profile_view.html', {})


# ____________________________________________________________ Filter users

def user_list(request):
    filter = UserInfoFilter(request.GET, queryset=UserInfo.objects.all())
    return render(request, 'dashboard.html', {'filter': filter})


# ____________________________________________________________ Search

def search(request):
    q = request.GET.get("q")
    print q
    if q:
       # use `__istartswith' for optimal search
       results = User.objects.filter(username__icontains=q)
    else:
       results = User.objects.all()     

    context = dict(results=results, q=q)
    return render(request, "dashboard_search.html", context)

# ____________________________________________________________ Filter



# ____________________________________________________________Tracker - Course



# ____________________________________________________________Tracker - Scorecard

def view_tracker(request):
    # if request.method == 'GET':
    #     form = Course_ScoreForm()
    # else:
    #     # A POST request: Handle Form Upload
    #     form = Course_ScoreForm(request.POST) # Bind data from request.POST into a PostForm

    #     # If data is valid, proceeds to create new profile post and redirect the user
    #     if form.is_valid():


    #         info = Course_ScoreForm()

    #         info.golfcourse_id = Course.id
    #         info.hole_01 = form.cleaned_data['hole_01']
    #         info.hole_02 = form.cleaned_data['hole_02']
    #         info.hole_03 = form.cleaned_data['hole_03']
    #         info.hole_04 = form.cleaned_data['hole_04']
    #         info.hole_05 = form.cleaned_data['hole_05']
    #         info.hole_06 = form.cleaned_data['hole_06']
    #         info.hole_07 = form.cleaned_data['hole_07']
    #         info.hole_08 = form.cleaned_data['hole_08']
    #         info.hole_09 = form.cleaned_data['hole_09']
    #         info.hole_10 = form.cleaned_data['hole_10']
    #         info.hole_11 = form.cleaned_data['hole_11']
    #         info.hole_12 = form.cleaned_data['hole_12']
    #         info.hole_13 = form.cleaned_data['hole_13']
    #         info.hole_14 = form.cleaned_data['hole_14']
    #         info.hole_15 = form.cleaned_data['hole_15']
    #         info.hole_16 = form.cleaned_data['hole_16']
    #         info.hole_17 = form.cleaned_data['hole_17']
    #         info.hole_18 = form.cleaned_data['hole_18']
            
       
    #         info.save()
    #         return HttpResponseRedirect('/dashboard/tracker/')

    return render(request, 'tracker.html', {})

# ____________________________________________________________Map

def show_map(request):
    return render(request, 'main-maps.html', {})

# ____________________________________________________________Calendar


# ____________________________________________________________Buddy List


# ____________________________________________________________Create Event



