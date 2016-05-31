from rest_framework import serializers
from .models import BlogEntry


class BlogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogEntry
        fields = (
            'title',
            'body_text',
            'comic',
            'date_created',
            'last_modified',
        )
