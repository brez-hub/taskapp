from django.conf.urls import url
from django.urls import include
from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('', cache_page(60)(views.index), name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('overview', views.overview, name='overview'),
    path('task-list', views.tasklist, name='task-list'),
    path('task-detail/<str:pk>', views.taskDetail, name='task-detail'),
    path('task-create', views.taskCreate, name='task-create'),
    path('task-update/<str:pk>', views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>', views.taskDelete, name='task-delete'),
]
