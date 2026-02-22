from django.contrib import admin

# Register your models here.
from .models import Student, Achievement, Category

admin.site.register(Student)
admin.site.register(Achievement)
admin.site.register(Category)
