from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    poster = models.ImageField(upload_to='posters/',null=True, blank=True)
    brochure = models.FileField(upload_to='brochures/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.event.title}"
