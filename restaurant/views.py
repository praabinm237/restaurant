from django.shortcuts import get_object_or_404
from .models import Table, Waiter, Order, Menu, Category, Reception
from .serializers import (
    TableSerializer, 
    WaiterSerializer, 
    OrderSerializer, 
    MenuSerializer, 
    CategorySerializer, 
    ReceptionSerializer
)
from rest_framework import mixins,generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TableList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,request):
        return self.list(request)
        
    def post(self,request):
        return self.create(request)
      
class TableDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
    
class WaiterList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,request):
        return self.list(request)
        
    def post(self,request):
        return self.create(request)
      
class WaiterDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
    
class OrderList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,request):
        return self.list(request)
        
    def post(self,request):
        return self.create(request)
      
class OrderDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
    
class MenuList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,request):
        return self.list(request)
        
    def post(self,request):
        return self.create(request)
      
class MenuDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
    
class CategoryList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,request):
        return self.list(request)
        
    def post(self,request):
        return self.create(request)
            
class CategoryDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
    
class ReceptionList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,request):
        return self.list(request)
        
    def post(self,request):
        return self.create(request)   
      
class ReceptionDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    

    

    

    
