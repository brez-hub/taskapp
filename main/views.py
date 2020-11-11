from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse, HttpResponse
from .serializers import TaskSerializer


def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверой'

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)
#Работа с JSON объектами

@api_view(['GET'])
def overview(request):
    main_urls = {
        'List':'/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(main_urls)

#(JSON) Список

@api_view(['GET'])
def tasklist(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)

#(JSON) Данные по ID

@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

#(JSON) Создание

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#(JSON) Изменение + Кеш + COOKIE для изменённой записи

@api_view(['POST'])
def taskUpdate(request, pk):
    if pk in request.COOKIES:
        tasks = Task.objects.order_by('id')
        return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})
    else:
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = redirect('/')
            response.set_cookie(pk, "update")
            return response
            return Response(serializer.data)

#(JSON) Удаление

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Данные удалены')