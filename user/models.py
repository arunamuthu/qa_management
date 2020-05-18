from django.db import models
from django.contrib.auth.models import AbstractUser


class Gender(models.Model):
    value = models.CharField(max_length = 15, unique = True)

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(blank=False, null=False, max_length=255)
    last_name = models.CharField(blank=False, null=False, max_length=255)
    date_of_birth = models.DateTimeField()
    gender = models.ForeignKey (Gender, on_delete = models.CASCADE, db_column = 'gender_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    user  = models.OneToOneField(Profile,on_delete=models.CASCADE, db_column = 'user_id')
    password = models.CharField(max_length=20)
    username = None
    status = models.CharField(max_length=20,default="inactive")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = []


class EmailAddress(models.Model):
    id = models.AutoField(primary_key=True)
    user  = models.ForeignKey(Profile,on_delete=models.CASCADE, db_column = 'user_id')
    email_id = models.EmailField(max_length=255,unique=True,null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MobileNumber(models.Model):
    id = models.AutoField(primary_key=True)
    user  = models.ForeignKey(Profile,on_delete=models.CASCADE, db_column = 'user_id')
    mobile_number = models.CharField(max_length=10, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

