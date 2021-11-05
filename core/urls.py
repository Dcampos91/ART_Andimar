from django.db import router
from django.urls import path, include
from .views import * 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('postura', PosturaTotalView, basename='TablaPostura'),

urlpatterns = [
    path('',home, name="home"),
    path('api/', include(router.urls)),
]