from django.contrib import admin

# Register your models here.
from employee_crud_app.models import Employee
class Employee_admin(admin.ModelAdmin):
    l = ['eno','ename','esal','eaddr']
admin.site.register(Employee,Employee_admin)
