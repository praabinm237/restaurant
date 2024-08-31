from rest_framework import serializers
from .models import Table, Waiter, Order, Menu, Category, Reception

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id','table_number','capacity','status']
        
class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = ['id','first_name','last_name','phone_number']
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','table','waiter','order_date_time','total_amount']
        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','name','description','price']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','menu','name']
        
class ReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reception
        fields = ['id','first_name','last_name','phone_number']