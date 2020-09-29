from django.shortcuts import render, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone




def tasks_list(request):
    tasks = Task.objects.filter(state='todo').order_by('created_at') 
    return render(request, 'personal_assistants/tasks.html', {'tasks': tasks})

def tasks_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'personal_assistants/tasks_detail.html', {'task': task})

def tasks_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('tasks_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'personal_assistants/tasks_new.html', {'form': form})

def task_status_update(request, pk):
    if request.method == "POST":
        task_s_u = Task.objects.get(pk=pk) 
        task_s_u.state = request.POST['state']
        task_s_u.save()
        return redirect('personal_assistants/tasks.html', {'task_s_u': task_s_u})

def tasks_old(request):
    tasks = Task.objects.filter(state='done').order_by('created_at') 
    return render(request, 'personal_assistants/tasks.html', {'tasks': tasks})
    
