from rest_framework import serializers
from django.contrib.auth.models import User
from home.models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        # fields = ('username', 'email','last_login')
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
