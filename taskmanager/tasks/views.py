from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Task


@login_required(login_url='accounts:login')
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        # TODO Add multiple assignees
        assignee = request.POST.get('assignee')
        assigned_to = User.objects.get(username=assignee)

        task = Task(title=title, description=description,
                    assigned_to=assigned_to, status=status, created_by=request.user)
        task.save()

        return redirect('accounts:home')

    # TODO Get users based on team
    users = User.objects.all()

    return render(request, 'create.html', {'users': users})
