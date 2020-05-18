from django.db import models
from  user.models import Profile

class EducationType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True,blank=False, null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Institution(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True,blank=False, null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True,blank=False, null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class EducationDetail(models.Model):
    id = models.AutoField(primary_key=True)
    education_type  = models.ForeignKey(EducationType,on_delete=models.CASCADE,db_column="education_type_id")
    institution  = models.ForeignKey(Institution,on_delete=models.CASCADE,db_column="institution_id")
    board  = models.ForeignKey(Board,on_delete=models.CASCADE,db_column="board_id")
    user  = models.ForeignKey(Profile,on_delete=models.CASCADE, db_column = 'user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)