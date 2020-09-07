from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasks_list, name='tasks_list'),
    path('tasks/<int:pk>/', views.tasks_detail, name='tasks_detail'),
    path('tasks/new/', views.tasks_new, name='tasks_new'),

]