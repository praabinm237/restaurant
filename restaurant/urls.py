
from django.urls import path
from .views import (
    TableList, TableDetail, 
    WaiterList, WaiterDetail,
    OrderList, OrderDetail,
    MenuList, MenuDetail,
    CategoryList, CategoryDetail,
    ReceptionList, ReceptionDetail,
)

urlpatterns = [
    path('table',TableList.as_view()),
    path('table/<pk>',TableDetail.as_view()),
    path('waiter',WaiterList.as_view()),
    path('waiter/<pk>',WaiterDetail.as_view()),
    path('order',OrderList.as_view()),
    path('order/<pk>',OrderDetail.as_view()),
    path('menu',MenuList.as_view()),
    path('menu/<pk>',MenuDetail.as_view()),
    path('category',CategoryList.as_view()),
    path('category/<pk>',CategoryDetail.as_view()),
    path('reception',ReceptionList.as_view()),
    path('reception/<pk>',ReceptionDetail.as_view()),
]
