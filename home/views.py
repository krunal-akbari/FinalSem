from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Customer, OrderItem, Product, Order, ShippingAddress, Wishlist, WishlistItem
from django.http import JsonResponse
from . import datamakker
import json
from django.contrib.auth.decorators import user_passes_test
import datetime


# Create your views here.
# all things are handle by context renaring so gfoh(get the **** out of here )

# {{{


def contactus(request):
    return render(request, 'contectus.html')


def favorite(request):
    return render(request, 'favorite.html')


def complate(request):
    print("paymant has been recesived sucessfully")
    return render(request, 'complate.html')


def payment(request):
    return render(request, 'payment.html')


def home(request): #randaring page
    return render(request, 'home.html')

# https://stackoverflow.com/questions/15998140/how-to-limit-a-view-to-superuser-only
@user_passes_test(lambda u:u.is_superuser)
def chart(request):
    return render(request, 'chart.html')


def status(request,orderid):
    order = Order.objects.get(id=orderid)
    date = order.expectedtime
    ctx = {"status":order.status,"id":order.id,"date":date}
    return render(request, 'status.html',ctx)


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
    # print(product)
    ctx = {"product": product}
    return render(request, 'details.html', ctx)


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

def order_sucess(request,id,trasection_id,**kwargs):
    order = Order.objects.get(id=id)
    order.trasection_id = trasection_id
    order.date_ordered = datetime.datetime.now()
    order.expectedtime = datetime.datetime.now() + datetime.timedelta(days=3)
    order.complate = True
    order.save()
    return render(request, 'order_sucess.html')

def order_details(request):
    
    order = Order.objects.all().filter(customer=request.user.customer,complate=True)
    ctx = {"orders": order}
    return render(request, 'order_details.html',ctx)
    # return render(request, 'order_details.html')

def order_cancel(request,id):
    order = Order.objects.get(id=id)
    order.delete()
    return redirect('/order_details')

