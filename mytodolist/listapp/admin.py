from django.contrib import admin

# Register your models here.
from .models import todolist
admin.site.register(todolist)