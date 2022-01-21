from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=False)
    name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=True)
    cat = models.CharField(max_length=200)
    subcat = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.tname

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    compete = models.BooleanField(default=False)
    trasection_id = models.CharField(max_length=100,null=True,blank=True)


    def __str__(self) -> str:
        return str(self.id)

    @property
    def get_cart_totle(self):
        orderitems = self.orderitem_set.all()
        totle = sum([item.get_totle for item in orderitems])
        return totle

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        totle = sum([item.quantity for item in orderitems])
        return totle

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0,null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    @property
    def get_totle(self):
        totle = self.product.price * self.quantity
        return totle

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.address}"

# wishlist
class Wishlist(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class WishlistItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    witchlists = models.ForeignKey(Wishlist,on_delete=models.CASCADE,null=True)
