from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=20)
    course_name = models.CharField(max_length=25)
    duration = models.IntegerField(default=0)
    seats = models.IntegerField(default=20)