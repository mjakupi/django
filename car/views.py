from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer

# Create your views here.
class CarView(APIView):

    def get(self, request):
        car = Car.objects.all()
        serializer = CarSerializer(car,many=True)


        return Response(serializer.data)

