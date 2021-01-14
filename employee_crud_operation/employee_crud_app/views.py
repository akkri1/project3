from django.shortcuts import render,redirect
from employee_crud_app.models import Employee
from employee_crud_app.forms import Employee_form

# Create your views here.
def display(request):
    e = Employee.objects.order_by('eno')
    d = {'emp':e}
    return render(request,'employee_crud_app/index.html',d)

def insert_view(request):
    f = Employee_form()
    if request.method == "POST":
        f = Employee_form(request.POST)
        if f.is_valid():
            f.save(commit = True)
            return redirect("/")
    d = {'form' : f}
    return render(request,'employee_crud_app/insert.html',d)

def delete_view(request, id):
    e = Employee.objects.get(id = id)
    e.delete()
    return redirect("/")
def update_view(request,id):
    e = Employee.objects.get(id = id)

    if request.method == "POST":
        f = Employee_form(request.POST,instance = e)
        if f.is_valid():
            f.save(commit = True)
            return redirect("/")
    d = {'emp':e}

    return render(request,'employee_crud_app/update.html',d)
