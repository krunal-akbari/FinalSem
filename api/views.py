from django.shortcuts import render
from home.models import *
from .serializers import *

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def user_details(request, id, *args, **kwargs):

    try:
        user = User.objects.get(id=id)
        customer = Customer.objects.get(user=user)
        print(customer)
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
