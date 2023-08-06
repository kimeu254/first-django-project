from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_task/', views.new_task, name='new.task'),
    path('task/<int:pk>/', views.show_task, name='show.task'),
    path('edit/task/<int:pk>/', views.edit_task, name='edit.task'),
    path('update/task/<int:pk>', views.update_task, name='update.task'),
    path('delete/<int:pk>/', views.destroy_task, name='delete.task'),
    path('mark-complete/task/<int:pk>/', views.mark_complete, name='complete.task')
]
