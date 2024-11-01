from decimal import Decimal
from itertools import product

from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Product
from django.shortcuts import get_object_or_404, redirect, reverse
from .cart import Cart

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,"index.html", {'products':products})

def detail(request, id:int, title:str):
    product = get_object_or_404(Product,id=id)
    context = {'product' : product}
    return render(request,"detail.html", context)

def store(request):
    category = request.GET.get('category')
    if category is not None:
        products = Product.objects.filter(category__title=category)
    else:
        products = Product.objects.all()
    return render(request,"store.html", {'products':products})

def checkout(request):
    return render(request,"checkout.html")

@require_POST
def add_to_cart(request):
    product_id = request.POST.get("product_id")
    quantity = request.POST.get("quantity")
    update = True if request.POST.get("update") == "1" else False
    product = get_object_or_404(Product, id=product_id)

    cart = Cart(request)
    cart.add(product_id, str(product.price), int(quantity), update)

    return redirect(reverse('shop:cart_detail'))


def cart_detail(request):
    cart = Cart(request)

    if cart.product_ids:  # Check if there are any product IDs
        products = Product.objects.filter(id__in=cart.product_ids)

        # Add product details to each cart item
        for product in products:
            cart[str(product.id)]['product'] = product
            cart[str(product.id)]['total_price'] = Decimal(cart[str(product.id)]['price']) * cart[str(product.id)]['quantity']

    return render(request, "cart_detail.html", {'cart': cart})



def remove_from_cart(request, product_id):
    if Product.objects.filter(id=product_id).exists():
        cart = Cart(request)
        cart.remove(str(product_id))
        return redirect(reverse('shop:cart_detail'))

    raise Http404('product does not exists.')
