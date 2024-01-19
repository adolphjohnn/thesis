from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from django.utils import timezone


    


# Create your models here.
class QuestionAnswer(models.Model):
    code = models.CharField(primary_key=True, max_length=26)
    question = models.CharField(max_length=1000)
    answer = models.TextField()
    course = models.CharField(max_length=1000)
    year_level = models.CharField(max_length=1000)
    user = models.CharField(max_length=1000)
    session = models.CharField(max_length=1000)
    feedback = models.CharField(max_length=1000)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.question
    


# Create your models here.
class Rate(models.Model):
    code = models.CharField(primary_key=True, max_length=26)
    count = models.CharField(max_length=1000)
    course = models.CharField(max_length=1000)
    year_level = models.CharField(max_length=1000)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.course

class Feedback(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.TextField()
    feedback = models.CharField(max_length=1000)

    def __str__(self):
        return self.question