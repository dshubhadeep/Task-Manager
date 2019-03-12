from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Task


def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        username = request.POST.get('assignee')
        assignee = User.objects.get(username=username)

        task = Task(title=title, description=description,
                    assignee=assignee, status=status)
        task.save()

        return redirect('accounts:home')

    # TODO Get users based on team
    users = User.objects.all()

    return render(request, 'create.html', {'users': users})
