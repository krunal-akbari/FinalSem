from django.shortcuts import render
from home.models import *
from .serializers import *


# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def user_details(request,*args, **kwargs):
    customer = request.user.customer
    user = User.objects.all().filter(customer=customer)
    serializers = UserSerializer(user, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def get_order_details(request,id,*args, **kwargs):
    order = Order.objects.get(id=id)
    serializers = OrderSerializer(order, many=False)
    return Response(serializers.data)
