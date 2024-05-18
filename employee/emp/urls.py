from django.urls import path,include
from .views import *
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router = routers.DefaultRouter()
router.register(r'employee',EmployeeView,basename='employee')
router.register(r'lastmonth',LastMonthView,basename='lastmonth')
router.register(r'currentmonth',CurrentMonthView,basename='currentmonth')
urlpatterns = [
    path('',include(router.urls))
]