from django.contrib import admin
from .models import Table, Waiter, Order, Menu, Category, Reception

# Register your models here.

@admin.register(Table)
class Table(admin.ModelAdmin):
    list_display = [
        'table_number',
        'capacity',
        'status'
    ]
    list_editable = ['status']
    list_per_page = 10

@admin.register(Waiter)
class Waiter(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'phone_number',
    ]
    list_per_page = 10
    
@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = [
        'table',
        'waiter',
        'order_date_time',
        'total_amount',
    ]
    list_per_page = 10
    
@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    list_per_page = 10
    
@admin.register(Menu)
class Menu(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'price',
    ]
    list_filter = ['category']
    search_fields = ['name']
    list_per_page = 10
    
@admin.register(Reception)
class Reception(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'phone_number',
    ]
    list_per_page = 10
    
