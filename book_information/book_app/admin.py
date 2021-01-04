from django.contrib import admin
from book_app.models import Book

# Register your models here.
class Book_info(admin.ModelAdmin):
    list = ['tittle','author','isbn_number','published_date','no_of_copies_sold']
admin.site.register(Book,Book_info)
