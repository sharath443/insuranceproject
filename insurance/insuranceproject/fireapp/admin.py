
from django.contrib import admin
from .models import fire_mdl

@admin.register(fire_mdl)
class fdata(admin.ModelAdmin):
    list_display = ['owner_name']
