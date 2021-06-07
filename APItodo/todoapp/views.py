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


# Create your views here.

# class Projects(APIView):
#
#     def get(self, request, id):
#         project = Project.objects.filter(user=id)
#         serializer = ProjectSerializer(project, many=True)
#         return Response(serializer.data)
#
#
# class SubProjects(APIView):
#
#     def get(self, request, id):
#         sub_project = Sub_Projects.objects.filter(project=id)
#         serializer = Sub_ProjectsSerializer(sub_project, many=True)
#         return Response(serializer.data)

# class Projecto(APIView):
#
#     def post(self, request):
#         serializer = ProjectSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class SubProject(APIView):
#
#     def post(self, request):
#         serializer = Sub_ProjectsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SubProjectOptions(APIView):
#
#     def get(self, request, id):
#         sub_project = Sub_Projects.objects.filter(pk=id)
#         serializer = Sub_ProjectsSerializer(sub_project, many=True)
#         return Response(serializer.data)
#
#     def delete(self, request, id):
#         subproject = Sub_Projects.objects.filter(pk=id)
#         subproject.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ProjectOptions(APIView):
#     # permission_classes = [IsAuthenticated]
#     # authentication_classes = (TokenAuthentication,)
#
#     def get(self, request, id):
#         sub_project = Project.objects.filter(pk=id)
#         serializer = Sub_ProjectsSerializer(sub_project, many=True)
#         return Response(serializer.data)
#
#     def delete(self, request, id):
#         subproject = Project.objects.filter(pk=id)
#         subproject.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class CreateUser(APIView):

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetId(APIView):

    def get(self, request, token):
        user = Token.objects.get(key=token).user
        serializer = UserIdSerializer(user)
        return Response(serializer.data)

class Projects(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        project = Project.objects.filter(user = params['pk'])
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)


class SubProject(viewsets.ModelViewSet):
    queryset = Sub_Projects.objects.all()
    serializer_class = Sub_ProjectsSerializer

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        project = Sub_Projects.objects.filter(id = params['pk'])
        serializer = Sub_ProjectsSerializer(project, many=True)
        return Response(serializer.data)

class OneProject(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
