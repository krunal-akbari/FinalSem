from django.shortcuts import render ,HttpResponse
from django.contrib.auth.decorators import user_passes_test
import csv
from home.models import *
import home.datamakker as dmk
# Create your views here.

def csvrpt(request):
    response = HttpResponse(content_type='text/csv',headers={'Content-Disposition': 'attachment; filename="test.csv"'})
    writer = csv.writer(response)
    for x in dmk.a:
        writer.writerow([x,dmk.a[x]])


    return response

def jsonrpt(request):
    response = HttpResponse(content_type='application/json',headers={'Content-Disposition': 'attachment; filename="test.json"'})
    response.write(dmk.a)
    response.write(dmk.b)
    return response

def excelrpt(request):
    response = HttpResponse(content_type='application/vnd.ms-excel',headers={'Content-Disposition': 'attachment; filename="test.xls"'})
    response.write(dmk.a)
    return response



@user_passes_test(lambda u:u.is_superuser)
def chart(request):
    return render(request, 'chart.html')

