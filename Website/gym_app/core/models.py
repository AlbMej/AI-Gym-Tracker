from django.db import models
from django import forms

# Create your models here.

# class Loan(models.Model):
#     name="Loan"
#     BUSINESS_TYPES = (
#     ('', 'Choose...'),
#     ('FT', 'Food Truck'),
#     ('CON', 'Construction'),
#     ('OTH', 'Other')
#     )
#
#
#     first_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#     email = models.EmailField()
#
#     phone = models.CharField(max_length=32)
#
#     address = models.CharField(max_length=256)
#
#     city = models.CharField(max_length=64)
#     state = models.CharField(max_length=32)
#     zip_code = models.CharField(max_length=32)
#
#     amount_required = models.IntegerField() #label = 'Amount required'
#     business_type = models.CharField(max_length=3, choices=BUSINESS_TYPES)
#     years_in_business = models.IntegerField() #label='Years in business'
#     other = models.CharField(max_length=64)
#
#     agree = models.BooleanField()  #required=True