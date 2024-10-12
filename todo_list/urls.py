"""
URL configuration for todo_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app.views import HomeView, TagListView, AddTaskView, UpdateTaskView, DeleteTaskView, CompleteTaskView, AddTagView, UpdateTagView, DeleteTagView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('add_task/', AddTaskView.as_view(), name='add_task'),
    path('update_task/<int:pk>/', UpdateTaskView.as_view(), name='update_task'),
    path('delete_task/<int:pk>/', DeleteTaskView.as_view(), name='delete_task'),
    path('complete_task/<int:pk>/', CompleteTaskView.as_view(), name='complete_task'),
    path('add_tag/', AddTagView.as_view(), name='add_tag'),
    path('update_tag/<int:pk>/', UpdateTagView.as_view(), name='update_tag'),
    path('delete_tag/<int:pk>/', DeleteTagView.as_view(), name='delete_tag'),
]


