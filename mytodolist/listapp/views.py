
from django.shortcuts import render
from .models import todolist

# Create your views here.
def index(request):
    return render(request, 'listapp/index.html')

def about(request):
    return render(request, 'listapp/aboutus.html')

def contact(request):
    return render(request, 'listapp/contactus.html')

def services(request):
    return render(request, 'listapp/services.html')

def create_task(request):
    if request.method == "POST":
        task_title = request.POST.get('task-title')
        task_description = request.POST.get('task-desc')
        task_due_date = request.POST.get('due-date')
        new_task = todolist.objects.create(task_title=task_title, task_description=task_description, task_enddate=task_due_date)
        new_task.save()
    return render(request, 'mylist/create.html')

def view_tasks(request):
    tasks = todolist.objects.all()
    return render(request, 'mylist/read.html', {'tasks': tasks})

def edit_task(request, task_id):
    task = todolist.objects.get(id=task_id)
    if request.method == "POST":
        task.task_title = request.POST.get('task-title')
        task.task_description = request.POST.get('task-desc')
        task.task_enddate = request.POST.get('due-date')
        task.save()
    return render(request, 'mylist/update.html', {'task': task})

def delete_task(request, task_id):
    task = todolist.objects.get(id=task_id)
    task.delete()
    tasks = todolist.objects.all()
    return render(request, 'mylist/read.html', {'tasks': tasks})