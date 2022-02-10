from django.contrib import admin
from django.contrib.auth.models import User,Group
# Register your models here.
from .models import Customer,Order,OrderItem,Product,ShippingAddress,Wishlist,WishlistItem

# admin.site.unregister(User)
# admin.site.unregister(Group)

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(ShippingAddress)
admin.site.register(Wishlist)
admin.site.register(WishlistItem)
