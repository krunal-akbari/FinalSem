from django.urls import path
from . import views
 
urlpatterns = [
    path('csv', views.csvrpt, name='csv'),
    path('json', views.jsonrpt, name='json'),
    path('excel', views.excelrpt, name='excel'),
    path('chart',views.chart, name="chart"),
]
