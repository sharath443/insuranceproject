"""insuranceproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from insuranceapp import views as v1
from vechileapp import views as v2
from fireapp import views as v3


urlpatterns = [
    path('admin/', admin.site.urls),
    path('back',v1.back,name='back'),
    path('', v1.sign_up,name='sign_up'),
    path('home', v1.home, name='home'),
    path('show_data', v1.show_data, name='show_data'),
    path('update_data/<int:id>', v1.update_data, name='update_data'),
    path('delete_data/<int:id>', v1.delete_data, name='delete_data'),
    path('user_login', v1.user_login, name='user_login'),
    path('user_logout', v1.user_logout, name='user_logout'),
    path('vshow_data', v2.vshow_data, name='vshow_data'),
    path('fshow_data', v3.fshow_data, name='fshow_data'),
    path('fire_home',v3.home,name='fire_home')
]
