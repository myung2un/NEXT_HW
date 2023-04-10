from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
import datetime

def home(request):
    tasks = Post.objects.all()
    template_name = 'home.html'
    context_object_name = 'task'

    def get_tasks(self):
        now = datetime.datetime.now()
        tasks = task.filter(deadline=now).order_by('deadline')
        print(1111)
        print(tasks)
        now = datetime.datetime.now()
        for task in tasks:
            task.d_day = (task.deadline - now).days
        return tasks

    return render(request, 'home.html', {'tasks': tasks})


def new(request):
    if request.method == 'POST':
        new_task = Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            deadline=request.POST['deadline'], # 마감 기한 추가
        )
        return redirect('detail', new_task.pk)

    return render(request, 'new.html')

def detail(request, task_pk):
    task = Post.objects.get(pk=task_pk)

    return render(request, 'detail.html', {'task': task})\

def update(request, task_pk):
    task = Post.objects.get(pk=task_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=task_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'], # 마감 기한 추가

        )
        return redirect('detail', task.pk)

    return render(request, 'update.html', {'task': task})

def delete(request, task_pk):
    task = Post.objects.get(pk=task_pk)
    task.delete()

    return redirect('home')

