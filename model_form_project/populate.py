import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'model_form_project.settings')
django.setup()

from faker import Faker
from model_form_app.models import Student
f = Faker()
def populate(n):
    for i in range(n):
        froll = f.random_int(min = 1, max = 20)
        fname = f.name()
        fpercent = f.random_int(min = 1, max = 100)
        fdob = f.date_of_birth()
        femail = f.email()
        s = Student.objects.get_or_create(roll = froll,name = fname,percent = fpercent,dob = fdob,
        email = femail)

populate(20)
