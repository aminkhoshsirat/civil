from django.db.models.signals import post_save
from django.dispatch import receiver

from shop.models import Product, Cart, OrderProduct, Order


@receiver(post_save, sender=Product)
def sotf_delete_cart(sender, instance, created, **kwargs):
    if not created:
        product: Product = instance
        if product.deleted:
            carts = Cart.objects.filter(product=product)
            for cart in carts:
                cart.delete()

@receiver(post_save, sender=Product)
def sotf_delete_order_product(sender, instance, created, **kwargs):
    if not created:
        product: Product = instance
        if product.deleted:
            order_products = OrderProduct.objects.filter(product=product)
            for order_product in order_products:
                order_product.delete()

@receiver(post_save, sender=Order)
def sotf_delete_order_product(sender, instance, created, **kwargs):
    if not created:
        order: Order = instance
        if order.deleted:
            order_products = OrderProduct.objects.filter(product=order)
            for order_product in order_products:
                order_product.delete()