from django.db import models
from  user.models import Profile

class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True,blank=False, null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=False, max_length=255)
    state  = models.ForeignKey(State,on_delete=models.CASCADE,db_column="state_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    address_line1 = models.CharField(blank=False, null=False, max_length=255)
    address_line2 = models.CharField(blank=True, null=True,max_length=255)
    address_line3 = models.CharField(blank=True, null=True,max_length=255)
    landmark = models.CharField(max_length=255)
    pincode = models.CharField(max_length=6)
    state  = models.ForeignKey(State,on_delete=models.CASCADE,db_column="state_id")
    city  = models.ForeignKey(City,on_delete=models.CASCADE,db_column="city_id")
    user  = models.OneToOneField(Profile,on_delete=models.CASCADE, db_column = 'user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)