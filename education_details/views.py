from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.http.request import QueryDict
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import EducationType, Institution, Board, EducationDetail
from .serializers import EducationTypeSerializer, InstitutionSerializer, BoardSerializer, EducationDetailSerializer


class EducationTypeView(APIView):
    serializer_class = EducationTypeSerializer
    permission_classes = (AllowAny,)

    def get(self,request):
        if request.method == 'GET':
            educationType = EducationType.objects.all()
            serializer = EducationTypeSerializer(educationType, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            educationType_serializer = EducationTypeSerializer(data=request.data)
            if educationType_serializer.is_valid():
                educationType_serializer.save()
                return Response(educationType_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(educationType_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EducationTypeDetailView(APIView):

    serializer_class = EducationTypeSerializer
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return EducationType.objects.get(pk=pk)
        except EducationType.DoesNotExist:
            raise Http404

    def get(self, request, pk, **kwargs):
        educationType = self.get_object(pk)
        serializer = EducationTypeSerializer(educationType)
        return Response(serializer.data)

    def put(self, request, pk, **kwargs):
        educationType = self.get_object(pk)
        serializer = EducationTypeSerializer(educationType, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        educationType = self.get_object(pk)
        educationType.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class InstitutionView(APIView):
    serializer_class = InstitutionSerializer
    permission_classes = (AllowAny,)

    def get(self,request):
        if request.method == 'GET':
            institution = Institution.objects.all()
            serializer = InstitutionSerializer(institution, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            institution_serializer = InstitutionSerializer(data=request.data)
            if institution_serializer.is_valid():
                institution_serializer.save()
                return Response(institution_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(institution_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InstitutionDetailView(APIView):

    serializer_class = InstitutionSerializer
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Institution.objects.get(pk=pk)
        except Institution.DoesNotExist:
            raise Http404

    def get(self, request, pk, **kwargs):
        institution = self.get_object(pk)
        serializer = InstitutionSerializer(institution)
        return Response(serializer.data)

    def put(self, request, pk, **kwargs):
        institution = self.get_object(pk)
        serializer = InstitutionSerializer(institution, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        institution = self.get_object(pk)
        institution.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BoardView(APIView):
    serializer_class = BoardSerializer
    permission_classes = (AllowAny,)

    def get(self,request):
        if request.method == 'GET':
            board = Board.objects.all()
            serializer = BoardSerializer(board, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            board_serializer = BoardSerializer(data=request.data)
            if board_serializer.is_valid():
                board_serializer.save()
                return Response(board_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(board_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BoardDetailView(APIView):

    serializer_class = BoardSerializer
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            raise Http404

    def get(self, request, pk, **kwargs):
        board = self.get_object(pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    def put(self, request, pk, **kwargs):
        board = self.get_object(pk)
        serializer = BoardSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        board = self.get_object(pk)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EducationDetailView(APIView):
    serializer_class = EducationDetailSerializer
    permission_classes = (AllowAny,)

    def get(self,request):
        if request.method == 'GET':
            education_detail = EducationDetail.objects.all()
            serializer = EducationDetailSerializer(education_detail, many=True)
            return Response(serializer.data)
            


class UserEducationDetailView(APIView):

    serializer_class = EducationDetailSerializer
    permission_classes = (AllowAny,)

    def get_object_by_user(self, pk):
        try:
            return EducationDetail.objects.get(user=pk)
        except EducationDetail.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        education_detail = self.get_object_by_user(kwargs['user_id'])
        serializer = EducationDetailSerializer(education_detail)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        if request.method == 'PUT':
            education_detail_data = {
            'education_type': request.data['education_type'],
            'institution': request.data['institution'],
            'board': request.data['board'],
            'user': kwargs['user_id']
            }
            education_detail_serializer = EducationDetailSerializer(data=education_detail_data)
            if education_detail_serializer.is_valid():
                education_detail_serializer.save()
                return Response(education_detail_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(education_detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        education_detail = self.get_object(pk)
        education_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
