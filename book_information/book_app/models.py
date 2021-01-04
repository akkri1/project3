from django.db import models

# Create your models here.
class Book(models.Model):
    tittle = models.CharField(max_length = 20)
    author = models.CharField(max_length = 20)
    isbn_number = models.IntegerField()
    published_date = models.DateField()
    no_of_copies_sold = models.IntegerField()

    def __str__(self):
        return self.tittle
