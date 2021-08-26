from django.db import models

class fire_mdl(models.Model):
    polacy_no = models.IntegerField(null=True)
    type_property = models.CharField(max_length=10, null=True)
    owner_name = models.CharField(max_length=10, null=True)
    polacy = models.CharField(choices=[('50K', '50K'), ('2.5 Lakh', '2.5 Lakh'), ('10 Lakhs', '10 Lakhs'), ('life-time', 'life-time')], max_length=50)
    vehicle_wheel= models.IntegerField(null=True)
    cause_name = models.CharField(max_length=100, null=True)
    fire_date = models.DateField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=50, null=True)
    phone_no = models.IntegerField(null=True)
