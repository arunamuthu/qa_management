from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.http.request import QueryDict
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import State, City, Address
from .serializers import StateSerializer, CitySerializer , AddressSerializer


class StateView(APIView):
    serializer_class = StateSerializer
    permission_classes = (AllowAny,)

    def get(self,request):
        if request.method == 'GET':
            state = State.objects.all()
            serializer = StateSerializer(state, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            state_serializer = StateSerializer(data=request.data)
            if state_serializer.is_valid():
                state_serializer.save()
                return Response(state_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(state_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StateDetailView(APIView):

    serializer_class = StateSerializer
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return State.objects.get(pk=pk)
        except State.DoesNotExist:
            raise Http404

    def get(self, request, pk, **kwargs):
        state = self.get_object(pk)
        serializer = StateSerializer(state)
        return Response(serializer.data)

    def put(self, request, pk, **kwargs):
        state = self.get_object(pk)
        serializer = StateSerializer(state, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        state = self.get_object(pk)
        state.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CityView(APIView):
    serializer_class = CitySerializer
    permission_classes = (AllowAny,)

    def get(self,request, *args, **kwargs):
        if request.method == 'GET':
            city = City.objects.filter(state_id=kwargs['state_id'])
            serializer = CitySerializer(city, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            city_data = {
                'name': request.data['name'],
                'state': kwargs['state_id'],
            }
            city_serializer = CitySerializer(data=city_data)
            if city_serializer.is_valid():
                city_serializer.save()
                return Response(city_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(city_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CityDetailView(APIView):

    serializer_class = StateSerializer
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return City.objects.get(pk=pk)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, pk, **kwargs):
        city = self.get_object(pk)
        serializer = CitySerializer(city)
        return Response(serializer.data)

    def put(self, request, pk, **kwargs):
        city = self.get_object(pk)
        city_data = {
            'name': request.data['name'],
            'state_id': kwargs['state_id'],
        }
        serializer = CitySerializer(city, data=city_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        city = self.get_object(pk)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddressView(APIView):
    serializer_class = AddressSerializer
    permission_classes = (AllowAny,)

    def get(self,request):
        if request.method == 'GET':
            address = Address.objects.all()
            serializer = AddressSerializer(address, many=True)
            return Response(serializer.data)
            

class AddressDetailView(APIView):

    serializer_class = AddressSerializer
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except address.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        address = self.get_object(kwargs['user_id'])
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        address_data = {
        'address_line1': request.data['address_line1'],
        'address_line2': request.data['address_line2'],
        'address_line3': request.data['address_line3'],
        'landmark': request.data['landmark'],
        'pincode': request.data['pincode'],
        'state': request.data['state'],
        'city': request.data['city'],
        'user': kwargs['user_id']
        }
        serializer = AddressSerializer(data=address_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        address = self.get_object(pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

