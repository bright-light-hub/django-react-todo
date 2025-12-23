from django.urls import path
from . import views

urlpatterns = [
    # When the user visits 'todos/', call the todo_list view
    # path('', views.todo_list, name='todo_list'),
    # path('create/', views.todo_create, name='todo_create'),
    # path('update/<int:pk>/', views.todo_update, name='todo_update'),
    # path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
    path('api/todos/', views.TodoListAPI.as_view(), name='TodoListAPI'),
    path('api/todos/<int:pk>/', views.TodoDetailAPI.as_view(), name='todo_detail'),
]