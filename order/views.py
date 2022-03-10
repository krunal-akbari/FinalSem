from django.shortcuts import render, redirect
from home.models import *
from order.models import *
import datetime

# Create your views here.


def index(request):
    return render(request, 'index.html')


def order_sucess(request, id, trasection_id, **kwargs):
    order = Order.objects.get(id=id)
    order.trasection_id = trasection_id
    order.date_ordered = datetime.datetime.now()
    order.expectedtime = datetime.datetime.now() + datetime.timedelta(days=3)
    order.complate = True
    order.save()
    return render(request, 'order_sucess.html')


def order_details(request):
    order = Order.objects.all().filter(customer=request.user.customer,
                                       complate=True)
    ctx = {"orders": order}
    return render(request, 'order_details.html', ctx)
    # return render(request, 'order_details.html')


def order_cancel(request, id):
    order = Order.objects.get(id=id)
    cancel, created = CancelOrder.objects.get_or_create(id=id)
    cancel.customer = order.customer
    cancel.trasection_id = order.trasection_id
    cancel.cancelorder_time = datetime.datetime.now()
    cancel.save()
    order.delete()
    return redirect('/order_details')


def order_cancel_details(request, id):
    customer = request.user.customer
    cancel = CancelOrder.objects.all().filter(customer=customer)
    ctx = {"orders": cancel}
    return render(request, 'order_cancel_details.html', ctx)


def order_feedback(request, id):
    if request.method == 'POST':
        order = Order.objects.get(id=id)
        phoneno = request.POST.get('telephone')
        feedback = request.POST.get('complaint')
        email = request.POST.get('_replyto')
        fb , created= FeedBack.objects.get_or_create(customer=request.user.customer,email=email,phoneno=phoneno, feedback=feedback)
        fb.save()
        return redirect('/order/order_details')
    return render(request, 'feedback.html')


def complaint(request):
    return render(request, 'complain.html')

def cstatus(request, orderid):
    order = CancelOrder.objects.get(id=orderid)
    ctx = {"id": order.id}
    return render(request, 'cstatus.html', ctx)  # }}}
