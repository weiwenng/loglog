from django.db import models

# Create your models here.
class Todo(models.Model):
    subject = models.CharField(max_length=100)
    details = models.CharField(max_length=100)

class Menu(models.Model):
    title = models.CharField(max_length=100)
    minpax = models.IntegerField(default=25)
    price = models.IntegerField()