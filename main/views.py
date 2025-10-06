from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from main.models import Product
from django.urls import reverse
from main.forms import ProductForm
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)

    context = {
        'app' : 'Chill Kicks',
        'name': 'Ainur Fadhil',
        'class': 'PBP F',
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def show_products(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product,
        'product_id': product.id
    }

    return render(request, "prod_detail.html", context)

@login_required(login_url='/login')
def create_prod(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        prod_entry = form.save(commit=False)
        prod_entry.user = request.user  # set user dulu
        prod_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_prod.html", context)

def show_xml(request):
     products = Product.objects.all()
     xml_data = serializers.serialize("xml", products)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'user_id': product.user.id if product.user else None,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'brand': product.brand,
            'size': product.size,
            'color': product.color,
            'release_date': product.release_date.isoformat() if product.release_date else None,
            'reviews': product.reviews,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'brand': product.brand,
            'size': product.size,
            'color': product.color,
            'release_date': product.release_date.isoformat() if product.release_date else None,
            'reviews': product.reviews,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def edit_products(request, id):
    prod = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=prod)

    if form.is_valid() and request.method == 'POST':
        prod_entry = form.save(commit=False)
        prod_entry.user = request.user  # pastikan user tetap sama
        prod_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "edit_prod.html", context)

def delete_products(request, id):
    news = get_object_or_404(Product, pk=id)
    news.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    price = request.POST.get("price")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    brand = request.POST.get("brand")
    size = request.POST.get("size")
    color = request.POST.get("color")
    is_featured = request.POST.get("is_featured") == 'on'

    new_product = Product(
        name=name,
        description=description,
        price=price,
        category=category,
        thumbnail=thumbnail,
        brand=brand,
        size=size,
        color=color,
        is_featured=is_featured,
        user=request.user,
    )
    new_product.save()

    return JsonResponse({
        "status": "success",
        "id": str(new_product.id),
        "name": new_product.name,
        "price": new_product.price
    }, status=201)
