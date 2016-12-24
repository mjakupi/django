from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Town
from .serializers import CitiesSerializer


class TownsList(APIView):

    def get(self, request):
        Towns = Town.objects.all()
        serializer = CitiesSerializer(Towns, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = CitiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)