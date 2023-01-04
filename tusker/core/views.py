from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .models import Task
from .forms import TaskForm


# Create your views here.
@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)
    open_tasks = tasks.filter(status='O').count()
    closed_tasks = tasks.filter(status='C').count()
    progress_tasks = tasks.filter(status='P').count()

    context = {'tasks': tasks.count(), 'open': open_tasks, 'closed': closed_tasks, 'progress': progress_tasks}
    return render(request, 'core/index.html', context)


@login_required
def create(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            
            task.user = request.user
            task.start_date = timezone.now()
            if task.status == 'C':
                task.end_date = task.start_date
            
            try:
                task.save()
                messages.success(request, "Task created successfully")
            except Exception as e:
                messages.error(request, "It was not possible to save your task")
            
            return redirect('index')

    context = {'form': TaskForm()}
    return render(request, 'core/create.html', context)


@login_required
def read_all(request):
    tasks = Task.objects.filter(user=request.user)
    open_tasks = tasks.filter(status='O')
    closed_tasks = tasks.filter(status='C')
    progress_tasks = tasks.filter(status='P')

    context = {'categories': {
            'open_tasks': open_tasks,
            'progress_tasks': progress_tasks,
            'closed_tasks': closed_tasks
        }
    }
    return render(request, 'core/read_all.html', context)


@login_required
def update(request, id):
    task = get_object_or_404(Task, pk=id)

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            modified_task = form.save(commit=False)
            
            task.description = modified_task.description
            task.status = modified_task.status
            if task.status == 'C':
                task.end_date = timezone.now()
            else:
                task.end_date = None
            
            try:
                task.save()
                messages.success(request, 'Task modified successfully')
            except Exception as e:
                messages.error(request, 'It was not possible to modify your task')

            return redirect('read_all')

    context = {'form': TaskForm(instance=task)}
    return render(request, 'core/create.html', context)


@login_required
def delete(request, id):
    task = get_object_or_404(Task, pk=id)

    if request.method == 'POST':
        try:
            task.delete()
            messages.success(request, 'Task deleted successfully')
        except Exception as e:
            messages.error(request, 'It was not possible to delete your task')
        
        return redirect('read_all')

    context = {'task': task}
    return render(request, 'core/delete.html', context)