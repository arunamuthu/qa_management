from django.db import models
from  user.models import Profile
from  question.models import Question

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    answer = models.CharField(blank=False, null=False, max_length=5000)
    question  = models.ForeignKey(Question,on_delete=models.CASCADE,db_column="question_id")
    user  = models.ForeignKey(Profile,on_delete=models.CASCADE, db_column = 'user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Upvote(models.Model):
    id = models.AutoField(primary_key=True)
    answer  = models.ForeignKey(Answer,on_delete=models.CASCADE,db_column="answer_id")
    user  = models.ForeignKey(Profile,on_delete=models.CASCADE, db_column = 'user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Downvote(models.Model):
    id = models.AutoField(primary_key=True)
    answer  = models.ForeignKey(Answer,on_delete=models.CASCADE,db_column="answer_id")
    user  = models.ForeignKey(Profile,on_delete=models.CASCADE, db_column = 'user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
