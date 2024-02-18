from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.

def home(request):
     info=companyInformation.objects.all().first()
     return render(request, 'home.html')

def car(request):
    info=companyInformation.objects.all().first()
    products =product.objects.all()
    
    data={
       'info':info,
        'products':products
    }
    
    return render(request,'car.html',data)

def contact(request):
    
    return render(request,'contact.html')

def sign(request):
    return render(request,'sign.html')
