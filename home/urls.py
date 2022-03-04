from django.urls import path,re_path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('User_count',views.get_data, name="UserCount"),
    path('get_data/cat',views.get_cat_data, name="getdatacat"),
    path('update_item/',views.updateItem, name="update_item"),
    path('update_fav/',views.updateFav, name="update_fav"),
    path('detail/<int:product_id>/',views.details,name="detail"),
    path('cart',views.carts,name="carts"),
    path('checkout',views.checkout,name="checkout"),
    path('contactus',views.contactus,name="contactus"),
    path('favorite',views.favorite,name="favorite"),
    path('profile',views.profile,name="profile"),
    path('about',views.about,name="about"),
    path('status/<int:orderid>/',views.status,name="status"),
    path('payment',views.payment,name="payment"),
    path('complate',views.complate,name="sucess"),
    path('chart',views.chart, name="chart"),
]
