from django.contrib.auth.models import User
from .models import Project, Sub_Projects
from rest_framework import serializers

# The serializers are in charged of tranforming the json data o to python or the othere way around
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # we tell the class what type of model it is
        model = User
        # here are the fields that are going to be transformed
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email']
    # This code encripts the password of all users created
    extra_kwargs = {'password': {
        'write_only': True,
        'required': True
    }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
# the rest of the code are serializers for the models used for the api
class Sub_ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        # the model used was sub_projects
        model = Sub_Projects
        # by including __all__, it gets all the parametes of a model
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    notes = Sub_ProjectsSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = '__all__'
# this serializer was used to only serialize the field id of class "user"
class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']