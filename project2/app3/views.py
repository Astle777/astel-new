from django.shortcuts import render
from django.http import HttpResponse
def home (request):
    return render(request,'w1.html')
def home2(request):
    return render(request,'w2.html')
def home(request):
    d={"name":"Alen","Rollno":2}
    return render(request,'w1.html',d)

# Create your views here.
