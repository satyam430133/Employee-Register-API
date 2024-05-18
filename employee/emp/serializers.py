from rest_framework import serializers
from .models import DesignationModel,DepartmentModel,EmployeeModel

class DesignationSerializer(serializers.ModelSerializer):
    class Meta():
        model = DepartmentModel
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta():
        model = DesignationModel
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta():
        model = EmployeeModel
        fields = "__all__"
