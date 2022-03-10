from django.shortcuts import render
from django.views import View
from home.models import *
from .serializers import *
from xhtml2pdf import pisa
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from io import BytesIO
from home.models import *


@api_view(['GET', 'POST'])
def user_details(request, id, *args, **kwargs):

    try:
        user = User.objects.get(id=id)
        customer = Customer.objects.get(user=user)
    except Customer.DoesNotExist:
        return Response(status=404)
    if request.method == 'GET':
        serializers = CustomerSerializer(customer, many=False)
        return Response(serializers.data)
    if request.method == 'POST':
        serializers = CustomerSerializer(customer, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)


@api_view(['GET'])
def get_order_details(request, id, *args, **kwargs):
    order = Order.objects.all().filter(id=id)
    serializers = OrderSerializer(order, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def Item_details(request, id, *args, **kwargs):
    item = Product.objects.all().filter(pid=id)
    serializers = ItemSerializer(item, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def Cancel_order_details(request, *args, **kwargs):
    item = CancelOrder.objects.all()
    serializers = CancelSerializer(item, many=True)
    return Response(serializers.data)

def get_data(request,id):
    order = Order.objects.get(id=id)
    order_item = OrderItem.objects.filter(order=order)
    customer = request.user.customer
    user = User.objects.get(customer=customer)
    ctx = {'order': order, 'order_item': order_item, 'user': user.username}
    return ctx

def download_receipt(request, id):
    ctx = get_data(request,id)
    return render(request, 'download_receipt.html',ctx)

def render_to_pdf(tamplate_src,context_dict = {}):
    tamplate = get_template(tamplate_src)
    html = tamplate.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        return None


def ViewPDF(request,id):
    ctx = get_data(request,id)
    pdf = render_to_pdf('download_receipt.html',ctx)
    return HttpResponse(pdf, content_type='application/pdf')
