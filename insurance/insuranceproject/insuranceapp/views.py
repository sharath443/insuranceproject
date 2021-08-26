from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime,timedelta
import random
import string
from django.shortcuts import render
from .models import student_frm
from .forms import formclass
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from fireapp.models import fire_mdl
from vechileapp.models import vmodel

def back(request):
    response = HttpResponseRedirect('/home')
    response.delete_cookie('name')
    return response

def show_data(request):
    if request.method == 'POST':
        fm = formclass(request.POST)
        if fm.is_valid():
            polacy_no = int(''.join(random.choice(string.digits) for n in range(10)))
            name = fm.cleaned_data['name']
            fname = fm.cleaned_data['fname']
            age = fm.cleaned_data['age']
            gender = fm.cleaned_data['gender']
            date_brth = fm.cleaned_data['date_brth']
            email = fm.cleaned_data['email']
            address = fm.cleaned_data['address']
            phone_no = fm.cleaned_data['phone_no']
            reg = student_frm(polacy_no=polacy_no, name=name, fname=fname, age=age, gender=gender, date_brth=date_brth,
                              email=email, address=address, phone_no=phone_no, )
            reg.save()
            fm = formclass()

            response = HttpResponseRedirect('/show_data')
            response.set_cookie('name', f'{polacy_no} {name} please save your policy Number!!! Thank you !',expires= datetime.now() + timedelta(seconds=30))
            send_mail(
                f"My Insurance",
                f"{name} your polacy got registerd with polacy number {polacy_no}",
                settings.EMAIL_HOST_USER,
                [email]
            )
            return response

    else:
        fm = formclass()
        try:
            data = request.COOKIES['name']
        except:
            data = ''
    return render(request, 'health.html', {'forms': fm, 'data1': student_frm.objects.all(), 'data': data})


def update_data(request, id):
    pi = student_frm.objects.get(pk=id)
    fm = formclass(request.POST, instance=pi)
    if fm.is_valid():
        fm.save()
    else:
        pi = student_frm.objects.get(pk=id)
        fm = formclass(instance=pi)
    return render(request, 'index.html', {'forms': fm})


def delete_data(request, id):
    if request.method == 'POST':
        pi = student_frm.objects.get(pk=id)
        print(pi)
        pi.delete()
        return HttpResponseRedirect('/show_data')


def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, "created Done")
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form': fm})


def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        print(fm.is_valid())
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Succesfully !!!')
                return HttpResponseRedirect('home')
        else:
            fm = AuthenticationForm()
            return render(request, 'login.html', {'form': fm})
    else:
        fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/user_login')


def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                data = student_frm.objects.get(polacy_no=request.POST.get('polacy_no'))
                my_data = {'data': data, 'categories': 'health'}
                return render(request, 'home.html', my_data)
            except:
                try:
                    data1 = fire_mdl.objects.get(polacy_no=request.POST.get('polacy_no'))
                    my_data = {'data': data1, 'categories': 'fire'}
                    return render(request, 'home.html', my_data)
                except:
                    try:
                        data2 = vmodel.objects.get(polacy_no=request.POST.get('polacy_no'))
                        my_data = {'data': data2, 'categories': 'vmodel'}
                        return render(request, 'home.html', my_data)
                    except:
                        temp = 'Polcy Not Found'
                        return render(request, 'home.html', {'temp': temp})

    return render(request, 'home.html')
