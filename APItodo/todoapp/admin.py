from django.contrib import admin
from .models import Project, Sub_Projects

# Register your models here.

@admin.register(Project)
class ProjectModel(admin.ModelAdmin):
    list_filter = ('title',)

@admin.register(Sub_Projects)
class Sub_ProjectsModel(admin.ModelAdmin):
    list_filter = ('title', 'date')