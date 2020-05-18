from rest_framework import serializers
from .models import Answer,Upvote,Downvote

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"

class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = "__all__"

class DownvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Downvote
        fields = "__all__"