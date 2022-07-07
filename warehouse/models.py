from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Todo(models.Model):
    subject = models.CharField(max_length=100)
    details = models.CharField(max_length=100)

class Menu(models.Model):
    title = models.CharField(max_length=100)
    minpax = models.IntegerField(default=25)
    price = models.IntegerField()
    chosen = models.BooleanField(default=False)

class FoodList(models.Model):
    class Category(models.TextChoices):
        NOODLES = 'Noodles', _('Noodles')
        SANDWICH = 'Sandwich', _('Sandwich')
        CHICKEN = 'Chicken', _('Chicken')
        DIMSUM = 'Dimsum', _('Dimsum')
        PASTRY = 'Pastry', _('Pastry')
        DESSERT = 'Dessert', _('Dessert')
        DRINKS = 'Drinks', _('Drinks')

    category = models.CharField(max_length=100, choices=Category.choices, default=Category.DIMSUM)
    itemname = models.CharField(max_length=100) 

class Order(models.Model):
    foodlist = models.ForeignKey(FoodList, on_delete=models.CASCADE)