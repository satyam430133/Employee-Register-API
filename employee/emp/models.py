from django.db import models

# Create your models here.

desig = [
    ('CTO','CTO'),
    ('Software developer','Software developer'),
    ('Manager','Manager'),
    ('VP of Marketing','VP of Marketing'),
    ('Tech lead','Tech lead'),
    ('Computer engineer','Computer engineer'),
    ('CEO','CEO'),
    ('Director','Director'),
    ('Architect','Architect'),
    ('Product Manager','Product Manager'),
]
class DesignationModel(models.Model):
    Designation = models.CharField(max_length=100,choices=desig)
    def __str__(self):
        return str(self.Designation)

deprt = [
    ('Human Resources','Human Resources'),
    ('Sales','Sales'),
    ('Communication','Communication'),
    ('Finance Department','Finance Department'),
    ('Administration','Administration'),
    ('Development','Development'),
    ('Marketing','Marketing'),
    ('Research and development','Research and development'),
    ('Production department','Production department'),
    ('Technical Support','Technical Support'),

]

class DepartmentModel(models.Model):
    Department = models.CharField(max_length=100,choices=deprt)
    def __str__(self):
        return str(self.Department)
    
class EmployeeModel(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Date = models.DateField()
    Department = models.ManyToManyField(DepartmentModel)
    Designation = models.ManyToManyField(DesignationModel)