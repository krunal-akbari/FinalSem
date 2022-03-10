from django.contrib import admin
from django.urls import path,include 
from . import views

urlpatterns = [
    path('success/<int:id>/<str:trasection_id>',views.order_sucess,name="sucess"),
    path('order_details',views.order_details,name="order_details"),
    path('order_cancel/<int:id>',views.order_cancel,name="order_cancel"),
    path('order_cancel_details/<int:id>',views.order_cancel_details,name="order_cancel_details"),
    path('feedback/<int:id>/',views.order_feedback,name="order_feedback"),
    path('cstatus/<int:orderid>/',views.cstatus,name="cancelstatus"),
]

