from django.shortcuts import render
from book_app.models import Book
# Create your views here.
def book_list(request):
    bk = Book.objects.all()
    dic = {'book':bk}
    return render(request,'book_app/index.html',dic)
