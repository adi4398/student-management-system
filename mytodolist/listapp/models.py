from django.db import models

# Create your models here.
class todolist(models.Model):
    task_title = models.CharField(max_length=200)
    task_description = models.TextField()
    task_enddate = models.DateField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)

    def __str__(self):
        return self.task_title
