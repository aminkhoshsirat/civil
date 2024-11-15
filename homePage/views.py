from itertools import product
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Product, Order, OrderProduct
from django.shortcuts import get_object_or_404, redirect, reverse
from .cart import Cart
from .forms import OrderForm
import json
import requests

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

@login_required
def checkout(request):
    try:
        Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect(reverse('accounts:edit_profile') + '?next=51' + reverse('homePage:checkout'))
    cart = Cart(request)
    if request.method == "POST":
        different_address = request.POST.get('different_address')

        if different_address:
            Order_form = OrderForm(request.POST)
            if not Order_form.is_valid():
                return render(request,"checkout.html")

            order = save_order_different(Order_form, cart, request)
            cart.clear()
            return redirect(reverse('homePage:to_bank', args=[order.id]))

        order = save_order_user(cart, request)
        cart.clear()
        return redirect(reverse('homePage:to_bank', args=[order.id]))

    context = { 'provinces':Province.objects.all()}
    return render(request,'checkout.html', context=context)

def to_bank(request, order_id):
    order =get_object_or_404(Order, id=order_id, status__isnull=True)
    data = {
        'MerchantID': settings.ZARINPAL_MERCHANT_ID,
        'Amount': order.total_price,
        'Description': f'sandbox, order:{order.id}',
        'CallbackURL': settings.ZARINPAL_CALLBACK_URL,
    }
    data = json.dumps(data)

    headers = {'content-type':'application/json', 'content-length':str(len(data))}
    try:
        response = requests.post(settings.ZARINPAL_REQUEST, data=data, headers=headers, timeout=10)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                authority = response['Authority']
                return redirect(settings.ZARINPAL_STARTPAY + authority)
            else:
                return render(request, 'to_bank.html', context={'error':f'status error code: {response["Status"]}'})
        return render(request, 'to_bank.html', context={'error':f'response status code: {response.status_code}'})
    except requests.exceptions.Timeout:
        return render(request, 'to_bank.html', context={'error':'Time out error'})
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error details: {e}")
        return render(request, 'to_bank.html', context={'error': f'Connection Error: {str(e)}'})

import logging
logger = logging.getLogger(__name__)

def save_order_user(cart, request):
    logger.info("Attempting to create an order for user %s", request.user)

    # Create the order
    try:
        order = Order.objects.create(
            user=request.user,
            total_price=cart.get_total_price,
            note=request.POST.get('note'),
            different_address=False,
            first_name=request.user.first_name,
            last_name=request.user.last_name,
            mobile=request.user.mobile,
            postal_code=request.user.profile.postal_code,
            address=request.user.profile.address,
            city_id=request.user.profile.city_id,
        )
        logger.info("Order created successfully with ID %s", order.id)

        # Create order products
        for item in cart:
            OrderProduct.objects.create(
                order=order,
                product_id=item['product_id'],
                quantity=item['quantity'],
                price=item['price']
            )
        return order

    except Exception as e:
        logger.error("Error creating order: %s", e)
        return None

def save_order_different(Order_form, cart, request):
    order = Order.objects.create(user=request.user,
                                 total_price=cart.get_total_price,
                                 note=request.POST.get('note'),
                                 different_address=True,
                                 first_name=Order_form.cleaned_data['first_name'],
                                 last_name=Order_form.cleaned_data['last_name'],
                                 mobile=Order_form.cleaned_data['mobile'],
                                 postal_code=Order_form.cleaned_data['postal_code'],
                                 address=Order_form.cleaned_data['address'],
                                 city_id=Order_form.cleaned_data['city'],
                                 )
    for item in cart:
        OrderProduct.objects.create(order=order, product_id=item['product_id'], quantity=item['quantity'],
                                    price=item['price'])
    return order

@require_POST
def add_to_cart(request):
    product_id = request.POST.get("product_id")
    quantity = request.POST.get("quantity")
    update = True if request.POST.get("update") == "1" else False
    product = get_object_or_404(Product, id=product_id)

    cart = Cart(request)
    cart.add(product_id, product.price, int(quantity), update)

    return redirect(reverse('homePage:cart_detail'))

def cart_detail(request):
    return render(request, "cart_detail.html")

def remove_from_cart(request, product_id):
    if Product.objects.filter(id=product_id).exists():
        cart = Cart(request)
        cart.remove(str(product_id))
        return redirect(reverse('homePage:cart_detail'))

    raise Http404('product does not exists.')
