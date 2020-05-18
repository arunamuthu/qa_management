from django.db import models
from  user.models import Profile
from  skill.models import SkillSet


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    statement = models.CharField(unique=True,blank=False, null=False, max_length=255)
    user  = models.ForeignKey(Profile,on_delete=models.CASCADE, db_column = 'user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class QuestionSkill(models.Model):
    id = models.AutoField(primary_key=True)
    question  = models.ForeignKey(Question,on_delete=models.CASCADE,db_column="question_id")
    skill  = models.ForeignKey(SkillSet,on_delete=models.CASCADE,db_column="skill_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
