from django.contrib import admin
from django.contrib.auth.models import User,Group
# Register your models here.
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('tname','price','stock','available')
    list_filter = ('cat',)
    list_editable = ('price','stock','available')
    empty_value_display = '-empty-'
    search_fields = ('tname','description')

class OrderAdmin(admin.ModelAdmin):
    # pass
    list_display = ('id','status','trasection_id')
    list_editable = ('status',)
    empty_value_display = '-empty-'

class CustomerAdmin(admin.ModelAdmin):
    # pass
    list_display = ('id','name','email','phoneno')
    # list_editable = ('name','email','phoneno','address')
    empty_value_display = '-empty-'

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Product,ProductAdmin)
admin.site.register(ShippingAddress)
admin.site.register(Wishlist)
admin.site.register(WishlistItem)
admin.site.register(CancelOrder)
