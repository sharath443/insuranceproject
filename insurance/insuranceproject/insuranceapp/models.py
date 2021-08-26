from django.db import models


class student_frm(models.Model):
    polacy_no = models.IntegerField(null=True)
    name = models.CharField(max_length=10, null=True)
    fname = models.CharField(max_length=10, null=True)
    polacy = models.CharField(choices=[('10 K','10 K'),('50 K','50 K'), ('1 Lakhs','1 Lakhs'),('life-time','life-time')],max_length=50)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)
    date_brth = models.DateField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=50, null=True)
    phone_no = models.IntegerField(null=True)
