from django.db import models
# Create your models here.

class Table(models.Model):
    TABLE_AVAILABLE_CHOICE = 'AVAILABLE'
    TABLE_OCCUPIED_CHOICE = 'OCCUPIED'
    TABLE_RESERVED_CHOICE = 'RESERVED'
    
    TABLE_STATUS = [
        (TABLE_AVAILABLE_CHOICE,'AVAILABLE'),
        (TABLE_OCCUPIED_CHOICE,'OCCUPIED'),
        (TABLE_RESERVED_CHOICE,'RESERVED'),
    ]
    
    table_number = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    status = models.CharField(choices=TABLE_STATUS,default=TABLE_AVAILABLE_CHOICE,max_length=50)
    
    def __str__(self):
        return f'Table Id #{self.pk}'
    
class Waiter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
class Order(models.Model):
    table = models.ForeignKey(Table,on_delete=models.CASCADE)  
    waiter = models.ForeignKey(Waiter,on_delete=models.CASCADE)
    order_date_time = models.DateTimeField()
    total_amount = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.order_date_time}{self.total_amount}'
    
class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return f'{self.name}(description {self.description})(price {self.price})'
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,)
    
    def __str__(self) -> str:
        return self.name
    
class Reception(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f'{self.first_name}{self.last_name}(phone number : {self.phone_number})'