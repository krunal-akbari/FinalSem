from .models import *


# p         for     product 
# c         for     products totle in cart 
# item      for     the per product in cart
# coustomer for     getting the coustomer

def se_to_base(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complate=False)
        items = order.orderitem_set.all()
        chartItem = order.get_cart_items
    else:
        items = []
        order = {'get_cart_totle': 0, 'get_cart_items': 0}
        chartItem = order['get_cart_items']
    ctx = {"p": Product.objects.all(), "order": order,'c':chartItem,'items':items,'coustomer':customer}
    return {'base_ctx': ctx}
