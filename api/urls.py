from django.urls import path
from . import views
 
urlpatterns = [
    path('user/', views.user_details),
    path('order/<int:id>/', views.get_order_details),
]
