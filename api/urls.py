from django.urls import path
from . import views
 
urlpatterns = [
    path('user/<int:id>/', views.user_details),
    path('user/update/<int:id>/', views.user_update),
    path('order/<int:id>/', views.get_order_details),
]
