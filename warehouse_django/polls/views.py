from django.shortcuts import render, redirect
from .models import Products, Brands, Locations

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

def product_edit(request, id):
    product = Products.objects.get(id=id)
    brands = Brands.objects.all()

    data = {
        'data': product,
        'brands': brands,
    }

    return render(request, "product/edit.html", data)

def product_update(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        brand_id = request.POST['brand_id']

        product = Products.objects.get(id=id)
        product.name = name
        product.price = price
        product.description = description
        product.brand_id = int(brand_id)
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

def brand_edit(request, id):
    brand = Brands.objects.get(id=id)

    data = {
        'data': brand,
    }

    return render(request, "brand/edit.html", data)

def brand_update(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        email = request.POST['email']
        website = request.POST['website']
        phone = request.POST['phone']
        address = request.POST['address']

        brand = Brands.objects.get(id=id)
        brand.name = name
        brand.description = description
        brand.email = email
        brand.website = website
        brand.phone = phone
        brand.address = address
        brand.save()

    return redirect('brand.list')

def brand_delete(request, id):
    brand = Brands.objects.get(id=id)
    brand.delete()

    return redirect('brand.list')

def location_list(request):
    data = {
        'title':'Location List',
        'data': Locations.objects.all()
    }

    return render(request, "location/index.html", data)

def location_create(request):
    return render(request, "location/create.html")

def location_save(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        phone = request.POST['phone']
        address = request.POST['address']

        location = Locations(name=name, description=description, phone=phone, address=address)
        location.save()

    return redirect('location.list')