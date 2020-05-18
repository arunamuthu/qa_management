from rest_framework import serializers
from .models import EducationType, Institution, Board, EducationDetail

class EducationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationType
        fields = "__all__"

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = "__all__"

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"

class EducationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDetail
        fields = "__all__"