from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path('create/', views.create_task, name='create'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('edit/', views.edit, name='edit'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('comment/<int:task_id>', views.post_comment, name='comment')
]
