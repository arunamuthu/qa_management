from rest_framework import serializers
from .models import Question, QuestionSkill

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class QuestionSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionSkill
        fields = "__all__"

