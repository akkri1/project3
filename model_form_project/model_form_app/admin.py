from django.contrib import admin

# Register your models here.
from model_form_app.models import Student
class StudentAdmin(admin.ModelAdmin):
    l = ['roll','name','percent','dob','email']
admin.site.register(Student,StudentAdmin)
