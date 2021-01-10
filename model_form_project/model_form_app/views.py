from django.shortcuts import render

# Create your views here.
from model_form_app.models import Student
def view1(request):
    s = Student.objects.all()
    d = {'stud':s}
    return render(request,'model_form_app/index.html',d)
    
