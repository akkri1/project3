from django.db import models

# Create your models here.
class Employee(models.Model):
    Eid = models.IntegerField()
    Ename = models.CharField(max_length = 20)
    Eage = models.IntegerField()
    Esal = models.IntegerField()
    Desig = models.CharField(max_length = 30)

    def __str__(self):
        return self.Ename
