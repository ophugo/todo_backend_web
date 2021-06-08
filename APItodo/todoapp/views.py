from django.shortcuts import render, get_list_or_404
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import ProjectSerializer, Sub_ProjectsSerializer, UserSerializer, UserIdSerializer
from .models import Project, Sub_Projects
from rest_framework.decorators import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# The views are used for the api and they are in charged of sending the information and receiving it

# this api view if in charge of creating the users
class CreateUser(APIView):

    def post(self, request, format=None):
        # userSerlializer get the json and transformes it to python
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# This view is in charge or getting the user id
class GetId(APIView):

    def get(self, request, token):
        # here we used the token to obtain the id of the person thats logged in
        user = Token.objects.get(key=token).user
        # The information was obtained and serialized(all the serializers are in the serializer.py)
        serializer = UserIdSerializer(user)
        # returns the json.id
        return Response(serializer.data)

# the projects view is in charge of the main REST functions
class Projects(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        project = Project.objects.filter(user = params['pk'])
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

# the subProject view is in charge of the main REST functions
class SubProject(viewsets.ModelViewSet):
    queryset = Sub_Projects.objects.all()
    serializer_class = Sub_ProjectsSerializer

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        project = Sub_Projects.objects.filter(id = params['pk'])
        serializer = Sub_ProjectsSerializer(project, many=True)
        return Response(serializer.data)

# specialized view for getting the projects by the user id
class OneProject(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# specialized view for getting the subprojects by project id
class SubProjectTarea(viewsets.ModelViewSet):
    queryset = Sub_Projects.objects.all()
    serializer_class = Sub_ProjectsSerializer

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        project = Sub_Projects.objects.filter(project = params['pk'])
        serializer = Sub_ProjectsSerializer(project, many=True)
        return Response(serializer.data)
