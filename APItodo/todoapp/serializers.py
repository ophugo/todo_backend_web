from django.contrib.auth.models import User
from .models import Project, Sub_Projects
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email']

    extra_kwargs = {'password': {
        'write_only': True,
        'required': True
    }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class Sub_ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Projects
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    notes = Sub_ProjectsSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = '__all__'

class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']