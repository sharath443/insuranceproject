from django.contrib import admin
from .models import vmodel
# Register your models here.
@admin.register(vmodel)
class vdata(admin.ModelAdmin):
    list_display = ['id']

