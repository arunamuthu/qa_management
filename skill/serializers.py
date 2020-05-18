from rest_framework import serializers
from .models import SkillSet, AreaOfInterest

class SkillSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillSet
        fields = "__all__"

class AreaOfInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaOfInterest
        fields = "__all__"
