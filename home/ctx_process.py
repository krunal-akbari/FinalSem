from .models import *
from django.shortcuts import redirect


# p         for     product
# c         for     products total in cart
# item      for     the per product in cart
# coustomer for     getting the coustomer


def se_to_base(request):



    if request.user.is_authenticated:# {{{
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complate=False)
        items = order.orderitem_set.all()
        chartItem = order.get_cart_items
        favItem = order.get_cart_items# }}}
        favorite, created = Wishlist.objects.get_or_create(customer=customer)
        fav_item = favorite.wishlistitem_set.all()
        fav_item_count = favorite.get_fav_item_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0,}
        chartItem = order['get_cart_items']
        fav_item_count = 0
        customer = []
        fav_item = []

    ctx = {
        "p": Product.objects.all(),
        "order": order,
        'c': chartItem,
        'items': items,
        'coustomer': customer,
        'fav_item':fav_item,
        'fav_item_total':fav_item_count,
    }
    return {'base_ctx': ctx}


