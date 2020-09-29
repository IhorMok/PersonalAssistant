from django.urls import path
from . import views

from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('tasks/', views.tasks_list, name='tasks_list'),
    path('tasks/<int:pk>/', views.tasks_detail, name='tasks_detail'),
    path('tasks/new/', views.tasks_new, name='tasks_new'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),
    path('tasks/<int:pk>/status', views.task_status_update, name='task_status_update'),
    path('tasks/old/', views.tasks_old, name='tasks_old'),

]

