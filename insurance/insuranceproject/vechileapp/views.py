from datetime import datetime,timedelta
import string
import random
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import vehicle_frm
from .models import vmodel

def vshow_data(request):
    if request.method == 'POST':
        fm = vehicle_frm(request.POST)
        if fm.is_valid():
            polacy_no = int(''.join(random.choice(string.digits) for n in range(10)))
            vehicle_no = fm.cleaned_data['vehicle_no']
            owner_name = fm.cleaned_data['owner_name']
            vehicle_wheel = fm.cleaned_data['vehicle_wheel']
            vehicle_name = fm.cleaned_data['vehicle_name']
            vehicle_date = fm.cleaned_data['vehicle_date']
            email = fm.cleaned_data['email']
            address = fm.cleaned_data['address']
            phone_no = fm.cleaned_data['phone_no']
            reg = vmodel(polacy_no=polacy_no, vehicle_no=vehicle_no, owner_name=owner_name, vehicle_wheel=vehicle_wheel,
                         vehicle_name=vehicle_name, vehicle_date=vehicle_date, email=email, address=address,
                         phone_no=phone_no, )
            reg.save()
            fm = vehicle_frm()

            response = HttpResponseRedirect('/vshow_data')
            response.set_cookie('name', f'{polacy_no} {owner_name} please save your policy Number!!! Thank you !',
                                expires=datetime.now() + timedelta(seconds=30))
            send_mail(
                f"My Insurance",
                f"{owner_name} your polacy got registerd with polacy number {polacy_no}",
                settings.EMAIL_HOST_USER,
                [email]
            )
            return response

    fm = vehicle_frm()
    try:
        data = request.COOKIES['name']
    except:
        data = ''
    return render(request, 'vehicle.html', {'forms': fm, 'data1': vmodel.objects.all(), 'data': data})