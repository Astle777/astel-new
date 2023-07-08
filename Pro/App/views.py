from django.shortcuts import render
from django.http import HttpResponse
from .models import item

# Create your views here.
def home(request):
    p=item.objects.all()
    return render(request,'home.html',{"k":p})

def product(request,product_id):
    p=item.objects.get(id=product_id)
    return render(request,'product.html',{"product_id":p})