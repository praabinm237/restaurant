
from django.urls import path
from rest_framework import routers
from core.views import UserViewSet,activate

router = routers.SimpleRouter()
router.register('user',UserViewSet)

urlpatterns = [
    path('activation',activate)
    ] + router.urls
