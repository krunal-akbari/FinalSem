from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Customer, OrderItem, Product, Order, ShippingAddress, Wishlist,WishlistItem
from django.http import JsonResponse

import json

# Create your views here.


def home(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     compete=False)
        items = order.orderitem_set.all()
        chartItem = order.get_cart_items
    else:
        items = []
        order = {'get_cart_totle': 0, 'get_cart_items': 0}
        chartItem = order['get_cart_items']
    ctx = {"p": Product.objects.all(), "cartItem": chartItem, "order": order}
    return render(request, 'home.html', ctx)


def chart(request):
    return render(request, 'carts.html')


def get_data(request):
    a = {
        "jan": 50,
        "fab": 40,
        "mar": 51,
        "apr": 40,
        "may": 100,
        "jun": 63,
    }
    return JsonResponse(a)


def get_cat_data(request):

    a = {"Mobile": 500, "Fan": 200}

    return JsonResponse(a)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(f'Action {action} , productId {productId}')

    # print("the problem arive from below")

    customer = request.user.customer
    product = Product.objects.get(pid=productId)
    order, created = Order.objects.get_or_create(customer=customer,
                                                 compete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order,
                                                         product=product)

    if action == "add":
        orderItem.quantity += 1
        orderItem.save()
    elif action == "remove":
        orderItem.quantity -= 1
        orderItem.save()
    elif action == "delete":
        orderItem.delete()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("item was added", safe=False)


def details(request, product_id):
    product = get_object_or_404(Product, pid=product_id)
    print(product)
    ctx = {"product": product}
    return render(request, 'details.html', ctx)


def carts(request):

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
    return render(request, 'cart.html', ctx)


def checkout(request):

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
    return render(request, 'checkout.html', ctx)


def contactus(request):
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

    return render(request, 'contectus.html', ctx)


def favorite(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Wishlist.objects.get_or_create(customer=customer)
        items =  order.wishlistitem_set.all()
    else:
        items = []
    ctx = {"items": items}
    return render(request, 'favorite.html', ctx)

def updateFav(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(f'Action {action} , productId {productId}')

    # print("the problem arive from below")

    customer = request.user.customer
    product = Product.objects.get(pid=productId)

    favorite,created = Wishlist.objects.get_or_create(customer=customer)
    favoriteItem,created = WishlistItem.objects.get_or_create(product=product,wishlists=favorite)

    # if action == "add":
        # favorite.quantity += 1
        # favorite.save()
    # elif action == "remove":
        # favorite.quantity -= 1
        # favorite.save()
    # elif action == "delete":
        # favorite.delete()

    # if favorite.quantity <= 0:
        # favorite.delete()

    return JsonResponse("item was added", safe=False)
