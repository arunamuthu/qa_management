from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import Profile,User,EmailAddress,MobileNumber
from .serializers import ProfileSerializer, UserSerializer,EmailAddressSerializer,MobileNumberSerializer,UserLoginSerializer


class ProfileView(APIView):

    serializer_class = ProfileSerializer
    permission_classes = (AllowAny,)

    def get(self,request):
        if request.method == 'GET':
            profile = Profile.objects.all()
            serializer = ProfileSerializer(profile, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            profile_serializer = ProfileSerializer(data=request.data)
            if profile_serializer.is_valid():
                profile_serializer.save()
                user_data = {
                    'password': request.data['password'],
                    'user': Profile.objects.get(id=profile_serializer.data['id']).id,
                }
                user_serializer = UserSerializer(data=user_data)
                if user_serializer.is_valid():
                    user_serializer.save()
                else:
                    Profile.objects.get(id=profile_serializer.data['id']).delete()
                    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                email_data = {
                    'email_id': request.data['email_id'],
                    'user': Profile.objects.get(id=profile_serializer.data['id']).id,
                }
                email_serializer = EmailAddressSerializer(data=email_data)
                if email_serializer.is_valid():
                    email_serializer.save()
                else:
                    Profile.objects.get(id=profile_serializer.data['id']).delete()
                    return Response(email_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
                mobile_data = {
                    'mobile_number': request.data['mobile_number'],
                    'user': Profile.objects.get(id=profile_serializer.data['id']).id,
                }
                mobile_serializer = MobileNumberSerializer(data=mobile_data)
                if mobile_serializer.is_valid():
                    mobile_serializer.save()
                else:
                    Profile.objects.get(id=profile_serializer.data['id']).delete()
                    return Response(mobile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
                return Response(profile_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetailView(APIView):

    serializer_class = ProfileSerializer
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserLoginView(APIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)