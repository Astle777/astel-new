from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import studentform
from app1.models import collage

def home(request):
    return render(request,'w1.html')

# Create your views here.
def list(request):
    p=collage.objects.all()
    return render(request,'w1.html',{"m" :p})

def form1(request):
    form=studentform()
    if request.method == 'POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return list(request)
        else:
            form=studentform()
    return render(request, 'form1.html',{"form": form})    

def form2(request):
    form=studentform()
    if request.method=="POST":
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return list(request)
    return render(request,"form2.html")
def form3(request):
    if(request.method=='POST'):
        k=request.POST['d']
        p=request.POST['col']
        t=request.POST['pin']
        o=collage.objects.create(Dptname=k,Collagename=p,Pincode=t)
        o.save()
        return list(request)
    return render(request,'form3.html')
        
        