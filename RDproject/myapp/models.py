from operator import mod
from pyexpat import model
from turtle import update
from django.db import models

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
