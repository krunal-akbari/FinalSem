from django.shortcuts import render
from home.models import *
from .serializers import *


# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def user_details(request,id,*args, **kwargs):

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
        serializers = CustomerSerializer(customer,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

@api_view(['POST'])
def user_update(request,id,*args, **kwargs):
    user = User.objects.all().filter(id=id)
    serializers = CustomerSerializer(instance=user, many=False)
    return Response(serializers.data)


@api_view(['GET'])
def get_order_details(request,id,*args, **kwargs):
    order = Order.objects.all().filter(id=id)
    serializers = OrderSerializer(order, many=True)
    return Response(serializers.data)
