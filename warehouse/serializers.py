from .models import Menu, OrdertoFoodList, Todo, Order, FoodList
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our TodoSerializer
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Todo
        # the fields that should be included in the serialized output
        fields = ['id', 'subject', 'details']

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'minpax', 'price', 'chosen']

class FoodListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = FoodList
        fields = ['id', 'category', 'itemname']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'pax', 'delivery_place', 'delivery_date', 'delivery_time']

class OrdertoFoodListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = OrdertoFoodList
        fields = ['id', 'orders', 'foodlist']

