from django.shortcuts import render
from app1.models import stud
from app1.models import collage
from app1.forms import studentForm

# Create your views here.

def base(request):
    data=stud.objects.all()
    return render(request,'w1.html',{"k" :data})

def base1(request):
    data=collage.objects.all()
    return render(request,'w2.html',{"m" :data})

def list(request):
    p=stud.objects.all()
    return render(request,'w1.html',{"m" :p})

def form1(request):
    form=studentForm()
    if request.method == 'POST':
        form=studentForm(request.POST)
        if form.is_valid():
            form.save()
            return list(request)
        else:
            form=studentForm()
    return render(request, 'form1.html',{"form": form})        
        