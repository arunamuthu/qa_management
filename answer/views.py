from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.http.request import QueryDict
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import Answer, Upvote, Downvote
from .serializers import AnswerSerializer, UpvoteSerializer, DownvoteSerializer
from  user.models import Profile
from  question.models import Question


class AnswerView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = (AllowAny,)

    def get(self,request):
        if request.method == 'GET':
            answer = Answer.objects.all()
            serializer = AnswerSerializer(answer, many=True)
            return Response(serializer.data)


class AnswerDetailView(APIView):

    serializer_class = AnswerSerializer
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            raise Http404

    def get(self, request, pk, **kwargs):
        answer = self.get_object(pk)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)

    def put(self, request, pk, **kwargs):
        answer = self.get_object(pk)
        serializer = AnswerSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        answer = self.get_object(pk)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAnswerDetailView(APIView):

    serializer_class = AnswerSerializer
    permission_classes = (AllowAny,)

    def get_object_by_user(self, pk):
        try:
            return Answer.objects.filter(user=pk)
        except Answer.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        answer = self.get_object_by_user(kwargs['user_id'])
        serializer = AnswerSerializer(answer,many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            answer_data = {
                'answer': request.data['answer'],
                'question': request.data['question'],
                'user': kwargs['user_id'],
            }
            answer_serializer = AnswerSerializer(data=answer_data)
            if answer_serializer.is_valid():
                answer_serializer.save()
                return Response(answer_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(answer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionAnswerDetailView(APIView):

    serializer_class = AnswerSerializer
    permission_classes = (AllowAny,)

    def get_object_by_question(self, pk):
        try:
            return Answer.objects.filter(question=pk)
        except Answer.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        answer = self.get_object_by_question(kwargs['question_id'])
        serializer = AnswerSerializer(answer,many=True)
        return Response(serializer.data)


class UpvoteView(APIView):
    serializer_class = UpvoteSerializer
    permission_classes = (AllowAny,)

    def get(self,request, *args, **kwargs):
        if request.method == 'GET':
            upvote = Upvote.objects.get(user=kwargs['user_id'])
            serializer = UpvoteSerializer(upvote)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            upvote_data = {
                'answer': request.data['answer'],
                'user': kwargs['user_id'],
            }
            upvote_serializer = UpvoteSerializer(data=upvote_data)
            if upvote_serializer.is_valid():
                upvote_serializer.save()
                return Response(upvote_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(upvote_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpvoteDetailView(APIView):

    serializer_class = UpvoteSerializer
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Upvote.objects.get(pk=pk)
        except Upvote.DoesNotExist:
            raise Http404

    def get(self, request, pk, **kwargs):
        upvote = self.get_object(pk)
        serializer = UpvoteSerializer(upvote)
        return Response(serializer.data)

    def put(self, request, pk, **kwargs):
        upvote = self.get_object(pk)
        serializer = UpvoteSerializer(upvote, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        upvote = self.get_object(pk)
        upvote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class DownvoteView(APIView):
    serializer_class = DownvoteSerializer
    permission_classes = (AllowAny,)

    def get(self,request, *args, **kwargs):
        if request.method == 'GET':
            downvote = Downvote.objects.get(user=kwargs['user_id'])
            serializer = DownvoteSerializer(downvote)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            downvote_data = {
                'answer': request.data['answer'],
                'user': kwargs['user_id'],
            }
            downvote_serializer = DownvoteSerializer(data=downvote_data)
            if downvote_serializer.is_valid():
                downvote_serializer.save()
                return Response(downvote_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(downvote_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DownvoteDetailView(APIView):

    serializer_class = DownvoteSerializer
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Downvote.objects.get(pk=pk)
        except Downvote.DoesNotExist:
            raise Http404

    def get(self, request, pk, **kwargs):
        downvote = self.get_object(pk)
        serializer = DownvoteSerializer(downvote)
        return Response(serializer.data)

    def put(self, request, pk, **kwargs):
        downvote = self.get_object(pk)
        serializer = DownvoteSerializer(downvote, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        downvote = self.get_object(pk)
        downvote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class AnswerUpvoteView(APIView):
    serializer_class = UpvoteSerializer
    permission_classes = (AllowAny,)

    def get(self,request, *args, **kwargs):
        if request.method == 'GET':
            upvote = Upvote.objects.filter(answer=kwargs['answer_id']).count()
            return Response({
                'upvotes': upvote
            })

class AnswerDownvoteView(APIView):
    serializer_class = DownvoteSerializer
    permission_classes = (AllowAny,)

    def get(self,request, *args, **kwargs):
        if request.method == 'GET':
            downvote = Downvote.objects.filter(answer=kwargs['answer_id']).count()
            return Response({
                'downvotes': downvote
            })