from django.shortcuts import render

from DBApp1.models import Student

# Create your views here.
def view1(request):
    e = Student.objects.all()
    print(type(e))
    d = {'rec':e}
    return render(request,'DBApp1/index.html',d)
