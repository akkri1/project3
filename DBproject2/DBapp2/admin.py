from django.contrib import admin

from DBapp2.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    l = ['Eid','Ename','Eage','Esal','Desig']
admin.site.register(Employee,EmployeeAdmin)
