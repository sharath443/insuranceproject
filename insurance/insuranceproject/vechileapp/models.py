from django.db import models

class vmodel(models.Model):
    polacy_no = models.IntegerField(null=True)
    vehicle_no = models.SlugField(null=True)
    owner_name = models.CharField(max_length=50, null=True)
    polacy = models.CharField(choices=[('3K', '3K'), ('10K', '10K'), ('25Lakhs', '25Lakhs'), ('life-time', 'life-time')], max_length=50)
    vehicle_wheel = models.IntegerField(null=True)
    vehicle_name = models.CharField(max_length=50, null=True)
    vehicle_date = models.DateField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=50, null=True)
    phone_no = models.IntegerField(null=True)