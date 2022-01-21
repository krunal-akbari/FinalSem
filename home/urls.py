from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="user"),
    path('chart',views.chart, name="chart"),
    path('get_data',views.get_data, name="getdata"),
    path('get_data/cat',views.get_cat_data, name="getdatacat"),
    path('update_item/',views.updateItem, name=""),
    path('update_fav/',views.updateFav, name=""),
    path('detail/<int:product_id>/',views.details),
    path('cart',views.carts),
    path('checkout',views.checkout),
    path('contactus',views.contactus),
    path('favorite',views.favorite),
]
