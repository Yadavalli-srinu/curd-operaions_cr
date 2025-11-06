from django.shortcuts import render
from django.shortcuts import redirect
from app1.models import employee_model
from django.http import HttpResponse
from app1.forms import employee_form
def details(request):
    data = employee_model.objects.all()
    context = {
        "data":data
    }
    return render(request,'frontend_app1/home.html',context)

def emp_form(request):
    form = employee_form()
    if request.method=="POST":
        form = employee_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp_form1')
            
        else:
            return HttpResponse("Invalid data")
    else:
     content={
       "form":form
   }
    return render(request,'frontend_app1/info.html',content)

def first_page(request):
     return render(request,'frontend_app1/main.html')