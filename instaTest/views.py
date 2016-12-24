from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer


class PersonList(APIView):

    def get(self, request):
        Towns = Person.objects.all()
        serializer = PersonSerializer(Towns, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    person = Person.objects.all()

    context = {'person': person}

    return render(request, 'instaTest/index.html', context)