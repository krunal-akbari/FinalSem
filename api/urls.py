from django.urls import path
from . import views
 
urlpatterns = [
    path('user/<int:id>', views.user_details, name='user_details'),
    path('item/<int:id>',views.Item_details, name='item_details'),
    path('order/<int:id>/', views.get_order_details),
    path('cancelorder/<int:id>/', views.Cancel_order_details,name='cancelorder'),
    path('download_receipt/<int:id>/',views.download_receipt,name='download'),
    path('view/<int:id>/',views.ViewPDF,name='view')
]
