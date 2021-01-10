from django.shortcuts import render

# Create your views here.
from djnago_app.forms import Feedback
def student_feedback(request):
    f = Feedback()
    if request.method == "POST":
        f = Feedback(request.POST);
        if f.is_valid():
            name = f.cleaned_data['name']
            roll = f.cleaned_data['roll']
            email = f.cleaned_data['email']
            comments = f.cleaned_data['comments']
            d = {'name':name,'roll':roll,'email':email,'comments':comments}
            return render(request,'djnago_app/output.html',d)
    d = {'form':f}
    return render(request,'djnago_app/input.html',d)
