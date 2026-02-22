from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    register_number = models.CharField(max_length=50, unique=True)
    course = models.CharField(max_length=100)
    batch = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Achievement(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='achievements')
    title = models.CharField(max_length=200)
    description = models.TextField()
    proof = models.FileField(upload_to='proofs/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.title
    

