from django.shortcuts import render, redirect
from .models import Products, Brands

def index(request):
    data = {
        'title':'Dashboard'
    }   
    return render(request, "index.html", data) 

def product_list(request):
    result = Products.objects.all()

    data = {
        'data': result,
        'title':'Product List',
        'brands': Brands.objects.all()
    }   
    return render(request, "product/index.html", data)

def product_create(request):
    data = {
        'brands': Brands.objects.all(),
    }

    return render(request, "product/create.html", data)

def product_save(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        brand_id = request.POST['brand_id']

        product = Products(name=name, price=price, description=description, brand_id=int(brand_id))
        product.save()

    return redirect('product.list')

def brand_list(request):
    data = {
        'title':'Brand List',
        'data': Brands.objects.all()
    }

    return render(request, "brand/index.html", data)

def brand_create(request):
    return render(request, "brand/create.html")

def brand_save(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        email = request.POST['email']
        website = request.POST['website']
        phone = request.POST['phone']
        address = request.POST['address']

        brand = Brands(name=name, description=description, email=email, website=website, phone=phone, address=address)
        brand.save()

    return redirect('brand.list')