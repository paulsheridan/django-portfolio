from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'title',
            'description',
            'image',
            'published',
            'github_url',
            'project_url',
            'button_text',
        )
