
from .models import FoodList, OrdertoFoodList, Menu, Order
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import OrderSerializer, OrdertoFoodListSerializer, MenuSerializer, FoodListSerializer


# class TodoViewSet(viewsets.ModelViewSet):
#     ## The Main Query for the index route
#     queryset = Todo.objects.all()
#     # The serializer class for serializing output
#     serializer_class = TodoSerializer
#     # optional permission class set permission level
#     permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]
#     # permission_classes = [permissions.IsAuthenticated]

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.AllowAny]

class FoodListViewSet(viewsets.ModelViewSet):
    queryset = FoodList.objects.all()
    serializer_class = FoodListSerializer
    permission_classes = [permissions.AllowAny]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

class OrderToFoodListViewSet(viewsets.ModelViewSet):
    queryset = OrdertoFoodList.objects.all()
    serializer_class = OrdertoFoodListSerializer
    permission_classes = [permissions.AllowAny]