from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

class DegisnationView(viewsets.ModelViewSet):
    serializer_class = DesignationSerializer
    queryset = DesignationModel.objects.all()

class DepartmentView(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = DepartmentModel.objects.all()

class EmployeeView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = EmployeeModel.objects.all()

class LastMonthView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = EmployeeModel.objects.filter(Date__icontains = '2024-04-')

class CurrentMonthView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = EmployeeModel.objects.filter(Date__icontains = '2024-05-')