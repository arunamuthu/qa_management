from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.http.request import QueryDict
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import Question, QuestionSkill
from .serializers import QuestionSerializer, QuestionSkillSerializer
from  user.models import Profile
from  skill.models import SkillSet


class QuestionView(APIView):
    serializer_class = QuestionSerializer
    permission_classes = (AllowAny,)

    def get(self,request):
        if request.method == 'GET':
            question = Question.objects.all()
            serializer = QuestionSerializer(question, many=True)
            return Response(serializer.data)


class QuestionDetailView(APIView):

    serializer_class = QuestionSerializer
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, **kwargs):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, **kwargs):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserQuestionDetailView(APIView):

    serializer_class = QuestionSerializer
    permission_classes = (AllowAny,)

    def get_object_by_user(self, pk):
        try:
            return Question.objects.get(user=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        question = self.get_object_by_user(kwargs['user_id'])
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            question_data = {
                'statement': request.data['statement'],
                'user': kwargs['user_id'],
            }
            question_serializer = QuestionSerializer(data=question_data)
            if question_serializer.is_valid():
                question_serializer.save()
                skill_data = {
                    'skill': request.data['skill'],
                    'question': Question.objects.get(id=question_serializer.data['id']).id,
                }
                skill_serializer = QuestionSkillSerializer(data=skill_data)
                if skill_serializer.valid():
                    skill_serializer.save()
                else:
                    Question.objects.get(id=question_serializer.data['id']).delete()
                    return Response(skill_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
                return Response(question_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)