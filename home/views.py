from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Customer, OrderItem, Product, Order, ShippingAddress, Wishlist, WishlistItem
from django.http import JsonResponse

import json

# Create your views here.


def payment(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complate=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_items

    else:
        items = []
        order = {'get_cart_totle': 0, 'get_cart_items': 0}
        cartItem = order['get_cart_items']
    ctx = {'items': items, "order": order, "cartItem": cartItem}

    return render(request, 'payment.html', ctx)


def home(request):

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
    ctx = {"p": Product.objects.all(), "order": order,}
    return render(request, 'home.html', ctx)


def chart(request):
    return render(request, 'chart.html')


def status(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complate=False)
    else:
        order = []
    ctx = {"order": order}
    print(order)
    return render(request, 'status.html', ctx)


def get_data(request):
    a = {
        "jan": 50,
        "fab": 40,
        "mar": 51,
        "apr": 40,
        "may": 100,
        "a": 100,
        "b": 100,
        "jun": 63,
    }
    return JsonResponse(a)


def get_cat_data(request):

    a = {
        "Mobile": 500,
        "Fan": 200,
        "Laptop": 420,
        "T.V.": 600,
        "Spicker": 300,
    }

    return JsonResponse(a)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(pid=productId)
    order, created = Order.objects.get_or_create(customer=customer,
                                                 complate=False)
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
                                                     complate=False)
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
                                                     complate=False)
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
                                                     complate=False)
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
        favorite, created = Wishlist.objects.get_or_create(customer=customer)
        items = favorite.wishlistitem_set.all()
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

    favorite, created = Wishlist.objects.get_or_create(customer=customer,
                                                       complate=False)
    favoriteItem, created = WishlistItem.objects.get_or_create(
        product=product, wishlists=favorite)

    return JsonResponse("item was added", safe=False)


def profile(request):
    if request.user.is_authenticated:
        customer = request.user.customer
    else:
        customer = []
    ctx = {"c": customer}

    return render(request, 'profile.html', ctx)


def about(request):
    return render(request, 'aboutus.html')
