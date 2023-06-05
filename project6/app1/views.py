from django.shortcuts import render
from app1.models import Book
from app1.forms import Books
# Create your views here.
# def upload(request):
#     return render(request,'upload.html')   

# def show(request):
#     return render(request,'show.html')   


def home(request):
    return render(request,'home.html')   

def show(request):
    p=Book.objects.all()
    return render(request,'show.html',{"s":p})

def upload(request):
    form = Books()
    if(request.method == 'POST'):
      form=Books(request.POST,request.FILES)
      if form.is_valid():
        form.save()
        return home(request)
    return render(request,'upload.html',{"form":form})
    
    