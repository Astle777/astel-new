from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from app1.forms import CustomUserCreationForm
from app1.forms import Employee
from app1.models import Employees
# Create your views here.
def home(request):
    return render(request,'home.html')
def base(request):
    return render (request,'base.html')
def signup1(request):
    form=CustomUserCreationForm()
    if (request.method=='POST'):
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'signup1.html',{"form":form})
def user_login1(request):
    if(request.method=='POST'):
        name=request.POST['n']
        password=request.POST['p']
        user=authenticate(username=name,password=password)
        if user:
            login(request,user)
            return home(request)
        else:
            return HttpResponse('invalid user')
    return render(request,'login1.html')    
def user_logout1(request):
    logout(request)
    return user_login1(request)

# def employeedetails(request):
#     form = Employee()
#     if(request.method=='POST'):
#         form = Employee(request.POST)
#         if form.is_valid():
#             form.save()
#             return home(request)
#         else:
#             form = Employee
#     return render(request,'employeedetails.html',{"form":form})

def list(request):
    p=Employees.objects.all()
    return render(request,'view.html',{"k":p})
               
            
def employeedetails(request):
    if(request.method=='POST'):
        a = request.POST['employeeid']
        b= request.POST['employeename']
        c = request.POST['company']
        d = request.POST['Designation']
        e = request.POST['place']
        f = request.POST['salary']
        p = Employees.objects.create(employeeid=a,employeename=b,company=c,Designation=d,place=e,salary=f)
        p.save()
        return home(request)
    return render(request,'employeedetails.html')