from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
import random
from .forms import *

from login.models import CustomerModel
from home.models import Customer


# Create your views here.
def signin_up(request):
    return render(request, 'signin_up.html')


def otp(request):
    return render(request, 'otp.html')


def otpgenrater():
    digit = "1234567890ABCDEFGHIJKLMNOPQRSUVWXYZ"
    otp = ""
    for x in range(6):
        otp += random.choice(digit)
    return otp


def send_otp(request):
    email = request.GET.get('email')
    otp = otpgenrater()
    send_mail('subject',
              f'body {otp}',
              'krunal.oceanmtech@gmail.com', [email],
              fail_silently=False)
    return HttpResponse(otp)


def signin_ups(request):

    if request.user.is_authenticated:
        return redirect('user')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            if 'register' in request.POST:
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    c = Customer.objects.create(user=request.user)
                    c.save()
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request, 'Account was created for ' + user)

                    return redirect('login')
            if 'signin' in request.POST:
                username = request.POST.get('uemail')
                password = request.POST.get('upassword')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('user')
                else:
                    messages.info(request, 'Username OR password is incorrect')

        context = {'form': form}
        return render(request, 'signin_up.html', context)


    # if request.method == 'POST':
    # if 'register' in request.POST:
    # if request.POST.get('name') and request.POST.get('password') and request.POST.get('confpassword'):
    # username = request.POST.get('name')
    # password = request.POST.get('password')
    # u1 = CustomerModel(cname=username, password=password)
    # u1.save()
    # return redirect('/signin_up/otp/')
    # elif 'signin' in request.POST:
    # if request.POST.get('uemail') and request.POST.get('upassword'):
    # email = request.POST.get('uemail')
    # password = request.POST.get('upassword')
    # u = CustomerModel.objects.filter(email=email, password=password)
    # if u :
    # print("user found")
    # return redirect('/')
    # return render(request, 'signin_up.html', ctx)
