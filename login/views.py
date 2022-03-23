from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth import authenticate
import random
from .forms import *

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
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            if 'register' in request.POST:
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    name = form.cleaned_data.get('username')
                    user = User.objects.get(username=name)
                    c = Customer.objects.create(user=user)
                    c.save()

                    messages.success(request,
                                     'Account was created for ' + name)

                    return redirect('login_otp')
                else:
                    pass

            if 'signin' in request.POST:
                username = request.POST.get('uemail')
                password = request.POST.get('upassword')

                user = authenticate(request,
                                    username=username,
                                    password=password)

                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.info(request, 'Username OR password is incorrect')

        context = {'form': form}
        return render(request, 'signin_up.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')


def change_password(request):
    username = request.user.username
    user = authenticate(username=username, password='admin')
    if user is not None:
        user.set_password('kishan')
        print('Change password')

    else:
        print("user is not exist")

    return HttpResponse(user)
