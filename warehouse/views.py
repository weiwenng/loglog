
from .models import FoodList, Logistics, Menu, Order, OrdertoFoodList, OrdertoLogistics
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import LogisticsSerializer, OrderSerializer, MenuSerializer, FoodListSerializer, OrdertoFoodListSerializer, OrdertoLogisticsSerializer


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
    queryset = FoodList.objects.all().order_by('id')
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

class LogisticsViewSet(viewsets.ModelViewSet):
    queryset = Logistics.objects.all().order_by('category')
    serializer_class = LogisticsSerializer
    permission_class = [permissions.AllowAny]

class OrderToLogisticsViewSet(viewsets.ModelViewSet):
    queryset = OrdertoLogistics.objects.all().order_by('orders')
    serializer_class = OrdertoLogisticsSerializer
    permission_class = [permissions.AllowAny]
