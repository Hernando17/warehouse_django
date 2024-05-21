from django.shortcuts import render, redirect
from .models import Products, Brands, Locations, StockMoves, StockQuantity, Users
from django.contrib import messages
from django.db import DatabaseError, transaction
import datetime

def index(request):
    data = {
        'title':'Dashboard'
    }   
    return redirect('product.list')

def login(request):
    data = {
        'title':'Login'
    }   
    return render(request, "login.html", data)

def authenticate(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = Users.objects.filter(email=email, password=password).first()

        if user:
            request.session['user'] = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
            }
            return redirect('product.list')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid email or password')
            return redirect('login')
        
def register(request):
    data = {
        'title':'Register'
    }

    return render(request, "register.html", data)

def register_save(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        if Users.objects.filter(email=email).first():
            messages.add_message(request, messages.ERROR, 'Email already exists')
            return redirect('register')

        user = Users(name=name, email=email, password=password)
        user.save()

    return redirect('login')
    

def logout(request):
    if 'user' in request.session:
        del request.session['user']

    return redirect('login')

def product_list(request):
    if 'user' not in request.session:
        return redirect('login')

    result = Products.objects.all()

    data = {
        'data': result,
        'title':'Product List',
        'brands': Brands.objects.all()
    }   
    return render(request, "product/index.html", data)

def product_create(request):
    if 'user' not in request.session:
        return redirect('login')
    
    data = {
        'brands': Brands.objects.all(),
    }

    return render(request, "product/create.html", data)

def product_save(request):
    if 'user' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        brand_id = request.POST['brand_id']

        product = Products(name=name, price=price, description=description, brand_id=int(brand_id))
        product.save()

    return redirect('product.list')

def product_edit(request, id):
    if 'user' not in request.session:
        return redirect('login')

    product = Products.objects.get(id=id)
    brands = Brands.objects.all()

    data = {
        'data': product,
        'brands': brands,
    }

    return render(request, "product/edit.html", data)

def product_update(request, id):
    if 'user' not in request.session:
        return redirect('login')

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
        product.updated_at = datetime.datetime.now()
        product.save()

    return redirect('product.list')

def product_delete(request, id):
    if 'user' not in request.session:
        return redirect('login')
    
    product = Products.objects.get(id=id)
    product.delete()

    return redirect('product.list')

def product_detail(request, id):
    if 'user' not in request.session:
        return redirect('login')
    
    product = Products.objects.get(id=id)

    data = {
        'data': product,
    }

    return render(request, "product/detail.html", data)

def brand_list(request):
    if 'user' not in request.session:
        return redirect('login')

    data = {
        'title':'Brand List',
        'data': Brands.objects.all()
    }

    return render(request, "brand/index.html", data)

def brand_create(request):
    if 'user' not in request.session:
        return redirect('login')
    
    return render(request, "brand/create.html")

def brand_save(request):
    if 'user' not in request.session:
        return redirect('login')

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
    if 'user' not in request.session:
        return redirect('login')

    brand = Brands.objects.get(id=id)

    data = {
        'data': brand,
    }

    return render(request, "brand/edit.html", data)

def brand_update(request, id):
    if 'user' not in request.session:
        return redirect('login')

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
        brand.updated_at = datetime.datetime.now()
        brand.save()

    return redirect('brand.list')

def brand_delete(request, id):
    if 'user' not in request.session:
        return redirect('login')

    brand = Brands.objects.get(id=id)
    brand.delete()

    return redirect('brand.list')

def location_list(request):
    if 'user' not in request.session:
        return redirect('login')

    data = {
        'title':'Location List',
        'data': Locations.objects.all(),
        'stock_quantity': StockQuantity.objects.all()
    }

    return render(request, "location/index.html", data)

def location_create(request):
    if 'user' not in request.session:
        return redirect('login')
    
    return render(request, "location/create.html")

def location_save(request):
    if 'user' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        phone = request.POST['phone']
        address = request.POST['address']

        location = Locations(name=name, description=description, phone=phone, address=address)
        location.save()

    return redirect('location.list')

def location_edit(request, id):
    if 'user' not in request.session:
        return redirect('login')

    location = Locations.objects.get(id=id)

    data = {
        'data': location,
    }

    return render(request, "location/edit.html", data)

def location_update(request, id):
    if 'user' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        phone = request.POST['phone']
        address = request.POST['address']

        location = Locations.objects.get(id=id)
        location.name = name
        location.description = description
        location.phone = phone
        location.address = address
        location.updated_at = datetime.datetime.now()
        location.save()

    return redirect('location.list')

def location_delete(request, id):
    if 'user' not in request.session:
        return redirect('login')

    location = Locations.objects.get(id=id)
    location.delete()

    return redirect('location.list')

def stock_move_list(request):
    if 'user' not in request.session:
        return redirect('login')

    data = {
        'title':'Stock Move List',
        'data': StockMoves.objects.all()
    }

    return render(request, "stock_move/index.html", data)

def stock_move_create(request):
    if 'user' not in request.session:
        return redirect('login')

    data = {
        'products': Products.objects.all(),
        'locations': Locations.objects.all()
    }

    return render(request, "stock_move/create.html", data)

def stock_move_save(request):
    if 'user' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        product_id = request.POST['product_id']
        location_id = request.POST['location_id']
        location_dest_id = request.POST['location_dest_id']
        quantity = request.POST['quantity']

        stock_quantity_from = StockQuantity.objects.filter(product_id=product_id, location_id=location_id).first()
        stock_quantity_to = StockQuantity.objects.filter(product_id=product_id, location_id=location_dest_id).first()

        if stock_quantity_from.quantity < int(quantity):
            messages.add_message(request, messages.ERROR, 'Stock not enough')

            return redirect('stock_move.create')

        stock_move = StockMoves(product_id=product_id, location_id=location_id, location_dest_id=location_dest_id, quantity=quantity)
        stock_move.save()

        if stock_quantity_from:
            stock_quantity_from.quantity -= int(quantity)
            stock_quantity_from.updated_at = datetime.datetime.now()
            stock_quantity_from.save()
            
            if stock_quantity_to:
                stock_quantity_to.quantity += int(quantity)
                stock_quantity_to.updated_at = datetime.datetime.now()
                stock_quantity_to.save()
            else:
                stock_quantity = StockQuantity(product_id=product_id, location_id=location_dest_id, quantity=quantity)
                stock_quantity.updated_at = datetime.datetime.now()
                stock_quantity.save()
        else:
            messages.add_message(request, messages.ERROR, 'Product not found in source location') 
            return redirect('stock_move.create')  
        

    return redirect('stock_move.list')

def stock_quantity_list(request):
    if 'user' not in request.session:
        return redirect('login')

    data = {
        'title':'Stock Quantity List',
        'data': StockQuantity.objects.all()
    }

    return render(request, "stock_quantity/index.html", data)

def stock_quantity_create(request):
    if 'user' not in request.session:
        return redirect('login')

    data = {
        'products': Products.objects.all(),
        'locations': Locations.objects.all()
    }

    return render(request, "stock_quantity/create.html", data)

def stock_quantity_save(request):
    if 'user' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        product_id = request.POST['product_id']
        location_id = request.POST['location_id']
        quantity = request.POST['quantity']

        stock_quantity = StockQuantity(product_id=product_id, location_id=location_id, quantity=quantity)
        stock_quantity.save()

    return redirect('stock_quantity.list')

def stock_quantity_edit(request, id):
    if 'user' not in request.session:
        return redirect('login')

    stock_quantity = StockQuantity.objects.get(id=id)

    data = {
        'data': stock_quantity,
        'products': Products.objects.all(),
        'locations': Locations.objects.all()
    }

    return render(request, "stock_quantity/edit.html", data)

def stock_quantity_update(request, id):
    if 'user' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        product_id = request.POST['product_id']
        location_id = request.POST['location_id']
        quantity = request.POST['quantity']

        stock_quantity = StockQuantity.objects.get(id=id)
        stock_quantity.product_id = product_id
        stock_quantity.location_id = location_id
        stock_quantity.quantity = quantity
        stock_quantity.updated_at = datetime.datetime.now()
        stock_quantity.save()

    return redirect('stock_quantity.list')

def stock_quantity_delete(request, id):
    if 'user' not in request.session:
        return redirect('login')
    
    stock_quantity = StockQuantity.objects.get(id=id)
    stock_quantity.delete()

    return redirect('stock_quantity.list')