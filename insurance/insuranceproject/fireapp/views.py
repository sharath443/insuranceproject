from datetime import datetime, timedelta

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
import random
import string
from django.shortcuts import render
from .models import fire_mdl
from .forms import fire_frm

def fshow_data(request):
    if request.method == 'POST':
        fm = fire_frm(request.POST)
        if fm.is_valid():
            polacy_no = int(''.join(random.choice(string.digits) for n in range(10)))
            type_property = fm.cleaned_data['type_property']
            owner_name = fm.cleaned_data['owner_name']
            vehicle_wheel = fm.cleaned_data['vehicle_wheel']
            cause_name = fm.cleaned_data['cause_name']
            fire_date = fm.cleaned_data['fire_date']
            email = fm.cleaned_data['email']
            address = fm.cleaned_data['address']
            phone_no = fm.cleaned_data['phone_no']
            reg = fire_mdl(polacy_no=polacy_no, type_property=type_property, owner_name=owner_name,
                            vehicle_wheel=vehicle_wheel, cause_name=cause_name, fire_date=fire_date, email=email,
                            address=address, phone_no=phone_no, )
            reg.save()
            fm = fire_frm()
            response = HttpResponseRedirect('/fshow_data')
            response.set_cookie('name', f'{polacy_no} {owner_name} please save your policy Number!!! Thank you !',
                                expires=datetime.now() + timedelta(seconds=30))
            send_mail(
                f"My Insurance",
                f"{owner_name} your polacy got registerd with polacy number {polacy_no}",
                settings.EMAIL_HOST_USER,
                [email]
            )
            return response

    else:
        fm = fire_frm()
        try:
            data = request.COOKIES['name']
        except:
            data = ''
    return render(request, 'fire.html', {'forms': fm, 'data1': fire_mdl.objects.all(), 'data': data})


def home(request):
    if request.user.is_authenticated:
        print(request.method)
        if request.method == 'POST':
            data = fire_mdl.objects.get(polacy_no=request.POST.get('polacy_no'))
            my_data = {'data': data, 'categories': 'fire'}
            print(my_data)
            return render(request, 'home.html', my_data)
        return render(request, 'home.html')
