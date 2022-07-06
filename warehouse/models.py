from django.db import models

# Create your models here.
class Todo(models.Model):
    subject = models.CharField(max_length=100)
    details = models.CharField(max_length=100)

class Menu(models.Model):
    title = models.CharField(max_length=100)
    minpax = models.IntegerField(default=25)
    price = models.IntegerField()

class FoodList(models.Model):
    category = models.CharField(max_length=100)
    itemname = models.CharField(max_length=100)

class Order(models.Model):
    category = models.CharField(max_length=100)
    itemname = models.CharField(max_length=100)