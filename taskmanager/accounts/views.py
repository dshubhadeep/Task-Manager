from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Q
from django.shortcuts import redirect, render

from tasks.models import Task


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

    return render(request, 'home.html', {'tasks': tasks})
