from django.contrib import admin
from .models import *

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    field = "__all__"
admin.site.register(EmployeeModel,EmployeeAdmin)
admin.site.register(DepartmentModel)
admin.site.register(DesignationModel)