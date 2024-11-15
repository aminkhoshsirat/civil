from .cart import Cart
from .models import Product
from decimal import Decimal

def cart(request):
    cart_session = Cart(request)

    cart_session.update_cart_length()
    all_total_price = 0

    if cart_session.product_ids:
        products = Product.objects.filter(id__in=cart_session.product_ids)

        for product in products:
            cart_session[str(product.id)]['product'] = product
            cart_session[str(product.id)]['total_price'] = Decimal(cart_session[str(product.id)]['price']) * cart_session[str(product.id)]['quantity']

        for item in cart_session:
            item['total_price'] = Decimal(item['price']) * item['quantity']
            all_total_price += item['total_price']

    # Ensure these attributes are always set
    cart_session.all_total_price = all_total_price

    return {'cart':cart_session}