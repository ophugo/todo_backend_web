from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Django uses ORM Object Relational Mapping, this means that
# by creating the models and running the program it creates the tables for the data base

# Here we created the model that is in charge of creating the tokens for the users
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

#this line of code make the column email unique for the user table
User._meta.get_field('email')._unique = True

#This is the model for project
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

#This is the model for project
class Sub_Projects(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    completed = models.BooleanField(False)
    project = models.ForeignKey(Project, related_name='notes', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title