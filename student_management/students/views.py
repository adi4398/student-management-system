from django.contrib.auth.decorators import login_required
from .mongo import achievement_logs
from django.shortcuts import render, redirect
from .models import Student, Achievement, Category
from datetime import datetime


# Create your views here.

# SHOW ALL STUDENTS
from .models import Student, Achievement

def student_list(request):

    students = Student.objects.all()

    # Dashboard Counts
    total_students = Student.objects.count()
    active_students = Student.objects.filter(status="Active").count()
    inactive_students = Student.objects.filter(status="Inactive").count()
    total_achievements = Achievement.objects.count()

    context = {
        'students': students,
        'total_students': total_students,
        'active_students': active_students,
        'inactive_students': inactive_students,
        'total_achievements': total_achievements,
    }

    return render(request, 'students/student_list.html', context)


# ADD NEW STUDENT
def add_student(request):

    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            register_number=request.POST.get('register_number'),
            course=request.POST.get('course'),
            batch=request.POST.get('batch'),
            department=request.POST.get('department'),
            status=request.POST.get('status')
        )
        return redirect('student_list')

    return render(request, 'students/add_student.html')

# EDIT STUDENT
def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.register_number = request.POST.get('register_number')
        student.course = request.POST.get('course')
        student.batch = request.POST.get('batch')
        student.department = request.POST.get('department')
        student.status = request.POST.get('status')
        student.save()

        return redirect('student_list')

    return render(request, 'students/edit_student.html', {
        'student': student
    })


# DELETE STUDENT
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')


#view achivements
@login_required
def achievement_list(request):
    achievements = Achievement.objects.all()
    return render(request, 'students/achievement_list.html', {
        'achievements': achievements
    })

# add achivements
@login_required
def add_achievement(request):

    students = Student.objects.all()
    categories = Category.objects.all()

    if request.method == "POST":
        achievement = Achievement.objects.create(
            student_id=request.POST.get('student'),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            category_id=request.POST.get('category'),
            date=request.POST.get('date'),
            proof=request.FILES.get('proof')
        )

        achievement_logs.insert_one({
            "achievement_id": achievement.id,
            "student": achievement.student.name,
            "title": achievement.title,
            "category": achievement.category.name,
            "status": achievement.status,
            "action": "Created",
        })

        return redirect('achievement_list')

    return render(request, 'students/add_achievement.html', {
        'students': students,
        'categories': categories
    })

from django.shortcuts import get_object_or_404, redirect
from .models import Achievement

@login_required
def approve_achievement(request, pk):

    achievement = get_object_or_404(Achievement, pk=pk)
    achievement.status = "Approved"
    achievement.save()

    # ✅ MongoDB Approval Log
    achievement_logs.insert_one({
        "achievement_id": achievement.id,
        "student": achievement.student.name,
        "title": achievement.title,
        "action": "Approved",
        "status": achievement.status,
        "timestamp": datetime.now()
    })

    return redirect('achievement_list')


@login_required
def reject_achievement(request, pk):

    achievement = get_object_or_404(Achievement, pk=pk)
    achievement.status = "Rejected"
    achievement.save()

    # ✅ MongoDB Rejection Log
    achievement_logs.insert_one({
        "achievement_id": achievement.id,
        "student": achievement.student.name,
        "title": achievement.title,
        "action": "Rejected",
        "status": achievement.status,
        "timestamp": datetime.now()
    })

    return redirect('achievement_list')

from django.shortcuts import get_object_or_404

from django.shortcuts import render, redirect, get_object_or_404
from .models import Achievement, Student, Category
from .mongo import achievement_logs   # if using MongoDB logging

def edit_achievement(request, id):

    achievement = get_object_or_404(Achievement, id=id)
    students = Student.objects.all()
    categories = Category.objects.all()

    if request.method == "POST":

        achievement.student_id = request.POST.get('student')
        achievement.title = request.POST.get('title')
        achievement.description = request.POST.get('description')
        achievement.category_id = request.POST.get('category')
        achievement.date = request.POST.get('date')

        # update proof only if new file uploaded
        if request.FILES.get('proof'):
            achievement.proof = request.FILES.get('proof')

        achievement.save()

        # ✅ MongoDB edit logging (optional but recommended)
        achievement_logs.insert_one({
            "action": "Edited Achievement",
            "student": achievement.student.name,
            "title": achievement.title,
            "status": achievement.status
        })

        return redirect('achievement_list')

    return render(request, 'students/edit_achievement.html', {
        'achievement': achievement,
        'students': students,
        'categories': categories
 })




