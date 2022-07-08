
from .models import FoodList, Menu, Order, OrdertoFoodList
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import OrderSerializer, MenuSerializer, FoodListSerializer, OrdertoFoodListSerializer


# class TodoViewSet(viewsets.ModelViewSet):
#     ## The Main Query for the index route
#     queryset = Todo.objects.all()
#     # The serializer class for serializing output
#     serializer_class = TodoSerializer
#     # optional permission class set permission level
#     permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]
#     # permission_classes = [permissions.IsAuthenticated]

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all().order_by('id')
    serializer_class = MenuSerializer
    permission_classes = [permissions.AllowAny]

class FoodListViewSet(viewsets.ModelViewSet):
    queryset = FoodList.objects.all()
    serializer_class = FoodListSerializer
    permission_classes = [permissions.AllowAny]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

class OrderToFoodListViewSet(viewsets.ModelViewSet):
    queryset = OrdertoFoodList.objects.all().order_by('orders')
    serializer_class = OrdertoFoodListSerializer
    permission_classes = [permissions.AllowAny]