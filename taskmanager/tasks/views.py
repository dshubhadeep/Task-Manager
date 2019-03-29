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

# TODO Viewing permission
@login_required(login_url='accounts:login')
def detail(request, task_id):

    task = Task.objects.get(pk=task_id)

    # TODO Team viewing
    ''' Check whether user can view details of another task '''
    if request.user != task.created_by and request.user != task.assigned_to:
        return redirect('accounts:home')

    users = User.objects.all()

    statuses = [('P', 'Planned'), ('O', 'Ongoing'), ('D', 'Done')]

    return render(request, "detail.html", {
        "id": task_id, "task": task,
        "users": users, "statuses": statuses
    })


@login_required(login_url='accounts:login')
def edit(request):

    if request.method == 'POST':
        task = Task.objects.get(pk=request.POST.get("task_id"))
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        # TODO Add multiple assignees
        assignee = request.POST.get('assignee')
        assigned_to = User.objects.get(username=assignee)

        task.title = title
        task.description = description
        task.assigned_to = assigned_to
        task.status = status
        task.save()

        return redirect('accounts:home')

    return redirect('accounts:home')


@login_required(login_url='accounts:login')
def delete(request, task_id):
    Task.objects.get(pk=task_id).delete()
    return redirect('accounts:home')
