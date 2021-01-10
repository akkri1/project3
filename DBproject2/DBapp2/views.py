from django.shortcuts import render
from DBapp2.models import Employee

# Create your views here.
def Employees(request):
    e = Employee.objects.all()
    d = {'emp':e}
    return render(request,'DBapp2/index.html',d)
