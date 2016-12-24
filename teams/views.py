from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import JsonResponse
from django.http import Http404
from .models import Team
from .serializers import TeamSerializer

# Create your views here.

class TeamList(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get(self, request, format=None):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        teams = Team.objects.all()
        teams.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




"""
class TeamList(APIView):

    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        json.loads(request.body)
        serializer = TeamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
"""