from .models import *


def se_to_base(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     compete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_items
    else:
        items = []
        order = {'get_cart_totle': 0, 'get_cart_items': 0}
        cartItem = order['get_cart_items']
    ctx = {'items': items, "order": order, "cartItem": cartItem}
    return {'cartItem', ctx}
