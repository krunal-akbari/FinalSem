from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Customer, OrderItem, Product, Order, ShippingAddress, Wishlist, WishlistItem
from django.http import JsonResponse
from . import datamakker
import json

# Create your views here.
# all things are handle by context renaring so gfoh(get the **** out of here )

# {{{


def contactus(request):
    return render(request, 'contectus.html')


def payment(request):
    return render(request, 'payment.html')


def home(request):
    return render(request, 'home.html')


def chart(request):
    return render(request, 'chart.html')


def status(request):
    return render(request, 'status.html')


def about(request):
    return render(request, 'aboutus.html')


def carts(request):
    return render(request, 'cart.html')


def checkout(request):

    return render(request, 'checkout.html')


# }}}


#data getting and priting
def get_data(request):  # {{{
    return JsonResponse(datamakker.a)


def get_cat_data(request):
    return JsonResponse(datamakker.b)  # }}}


def profile(request):  #{{{
    if request.method == 'GET':
        if 'update' in request.GET:
            customer = request.user.customer
            fullname = request.GET.get('fullName')
            country = request.GET.get('country')
            address = request.GET.get('address')
            phoneno = request.GET.get('phone')
            email = request.GET.get('email')

            customer.name = fullname
            customer.email = email
            customer.state = country
            customer.address = address
            customer.phoneno = phoneno
            customer.save()

            return redirect('/profile')

    return render(request, 'profile.html')  # }}}


def updateItem(request):  # {{{
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

    return JsonResponse("item was added", safe=False)  # }}}


def details(request, product_id):
    product = get_object_or_404(Product, pid=product_id)
    print(product)
    ctx = {"product": product}
    return render(request, 'details.html', ctx)


def favorite(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        favorite, created = Wishlist.objects.get_or_create(customer=customer)
        items = favorite.wishlistitem_set.all()
    else:
        items = []
    ctx = {"items": items}
    return render(request, 'favorite.html', ctx
                  )


def updateFav(request):  # {{{
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    # print("the problem arive from below")

    customer = request.user.customer
    product = Product.objects.get(pid=productId)

    favorite, created = Wishlist.objects.get_or_create(customer=customer)
    favoriteItem, created = WishlistItem.objects.get_or_create(
        product=product, wishlists=favorite)

    if action == "add":
        favoriteItem.save()
    elif action == "delete":
        favoriteItem.delete()

    return JsonResponse("item was added", safe=False)  # }}}
