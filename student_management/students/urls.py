from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add-student/', views.add_student, name='add_student'),
    path('edit-student/<int:id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),
    path('achievements/', views.achievement_list, name='achievement_list'),
    path('add-achievement/', views.add_achievement, name='add_achievement'),
    path('approve-achievement/<int:pk>/', views.approve_achievement, name='approve_achievement'),
    path('reject-achievement/<int:pk>/', views.reject_achievement, name='reject_achievement'),
    path('edit-achievement/<int:id>/', views.edit_achievement, name='edit_achievement'),


]
