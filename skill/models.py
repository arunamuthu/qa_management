from django.db import models
from  user.models import Profile

class SkillSet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True,blank=False, null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AreaOfInterest(models.Model):
    id = models.AutoField(primary_key=True)
    skill  = models.ForeignKey(SkillSet,on_delete=models.CASCADE,db_column="skill_id")
    user  = models.ForeignKey(Profile,on_delete=models.CASCADE, db_column = 'user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
