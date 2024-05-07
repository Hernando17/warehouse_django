from django.shortcuts import render
from .models import Products

def index(request):
    result = Products.objects.all()
    print(result)
    data = {
        'data':result,
    }   
    return render(request,"index.html",data) 