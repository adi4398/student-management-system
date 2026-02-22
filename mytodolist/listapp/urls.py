from django.urls import path

from .views import index ,contact, about, services, create_task,view_tasks,edit_task, delete_task


urlpatterns = [
        
     path('', index, name='index'),
     path('about/', about, name='aboutus'),
     path('services/', services, name='contactus'),
     path('contact/', contact, name='services'), 
     path('create-task/', create_task, name='create_task'),
     path('view-tasks/',view_tasks,name='view_tasks'), 
     path('edit-task/<int:task_id>/', edit_task, name='edit_task'),
     path('delete-task/<int:task_id>/', delete_task, name='delete_task'),
     
]
