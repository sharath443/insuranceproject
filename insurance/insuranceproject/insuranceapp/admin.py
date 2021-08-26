from django.contrib import admin
from .models import student_frm


@admin.register(student_frm)
class sdata(admin.ModelAdmin):
    list_display = ['polacy_no','name']
