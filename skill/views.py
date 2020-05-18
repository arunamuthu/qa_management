from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.http.request import QueryDict
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import SkillSet,  AreaOfInterest
from .serializers import SkillSetSerializer,  AreaOfInterestSerializer


class SkillSetView(APIView):
    serializer_class = SkillSetSerializer
    permission_classes = (AllowAny,)

    def get(self,request):
        if request.method == 'GET':
            skill_set = SkillSet.objects.all()
            serializer = SkillSetSerializer(skill_set, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            skill_set_serializer = SkillSetSerializer(data=request.data)
            if skill_set_serializer.is_valid():
                skill_set_serializer.save()
                return Response(skill_set_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(skill_set_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SkillSetDetailView(APIView):

    serializer_class = SkillSetSerializer
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return SkillSet.objects.get(pk=pk)
        except SkillSet.DoesNotExist:
            raise Http404

    def get(self, request, pk, **kwargs):
        skill_set = self.get_object(pk)
        serializer = SkillSetSerializer(skill_set)
        return Response(serializer.data)

    def put(self, request, pk, **kwargs):
        skill_set = self.get_object(pk)
        serializer = SkillSetSerializer(skill_set, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        skill_set = self.get_object(pk)
        skill_set.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AreaOfInterestView(APIView):
    serializer_class = AreaOfInterestSerializer
    permission_classes = (AllowAny,)

    def get(self,request):
        if request.method == 'GET':
            area_of_interest = AreaOfInterest.objects.all()
            serializer = AreaOfInterestSerializer(area_of_interest, many=True)
            return Response(serializer.data)
            


class UserAreaOfInterestView(APIView):

    serializer_class = AreaOfInterestSerializer
    permission_classes = (AllowAny,)

    def get_object_by_user(self, pk):
        try:
            return AreaOfInterest.objects.filter(user=pk)
        except AreaOfInterest.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        area_of_interest = self.get_object_by_user(kwargs['user_id'])
        serializer = AreaOfInterestSerializer(area_of_interest, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        if request.method == 'PUT':
            area_of_interest_data = {
            'skill': request.data['skill'],
            'user': kwargs['user_id']
            }
            area_of_interest_serializer = AreaOfInterestSerializer(data=area_of_interest_data)
            if area_of_interest_serializer.is_valid():
                area_of_interest_serializer.save()
                return Response(area_of_interest_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(area_of_interest_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        area_of_interest = self.get_object_by_user(kwargs['user_id'])
        area_of_interest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

