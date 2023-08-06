from django.shortcuts import render, redirect
from .models import *
from .forms import TaskForm

# Create your views here.


def home(request):
    all_tasks = Task.objects.all().order_by('-date_created').values()

    context = {'all_tasks': all_tasks}
    return render(request, 'home.html', context)


def new_task(request):

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}

    return render(request, 'create.html', context)


def show_task(request, pk):

    task = Task.objects.get(id=pk)

    return render(request, 'task.html', {'task': task})


def edit_task(request, pk):

    task = Task.objects.get(id=pk)

    return render(request, 'edit.html', {'task': task})


def update_task(request, pk):

    task = Task.objects.get(id=pk)

    form = TaskForm(request.POST, instance=task)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'edit.html', {'task': task})


def destroy_task(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect('home')

    return render(request, 'delete.html', {'task': task})


def mark_complete(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.completed = True
        task.save()
        return redirect('home')

    return render(request, 'complete.html', {'task': task})

