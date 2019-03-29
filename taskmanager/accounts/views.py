from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render

from tasks.models import Task
from .models import Team


def register_view(request):

    # Check if user is authenticated, if yes then send to home
    if request.user.is_authenticated:
        return redirect('accounts:home')

    # Handle post request
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:home')
    else:
        # Handle login route
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):

    # Check if user is authenticated, if yes then send to home
    if request.user.is_authenticated:
        return redirect('accounts:home')

    # Handle post request
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            ''' Redirect based on next param '''
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))

            return redirect('accounts:home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


@login_required(login_url='accounts:login')
def home_view(request):

    # Get tasks assigned / created to user
    tasks = Task.objects.filter(
        Q(created_by=request.user) | Q(assigned_to=request.user))

    # Get teams of user
    teams = request.user.team_set.all()

    return render(request, 'home.html', {'tasks': tasks, 'teams': teams})


def create_team(request):

    if request.method == "POST":
        members_list = request.POST.getlist("members")
        team_name = request.POST.get("team_name")

        team = Team.objects.create(
            team_name=team_name, created_by=request.user)

        for member in members_list:
            team.members.add(User.objects.get(username=member))

        # Add creator to members
        team.members.add(request.user)

        team.save()

        # print(members)
        return redirect('accounts:home')

    users = User.objects.all().exclude(username=request.user.username)

    return render(request, "create_team.html", {'users': users})
