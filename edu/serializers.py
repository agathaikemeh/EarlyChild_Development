from rest_framework import serializers
from .models import Resource

class ResourceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Resource model.
    """
    class Meta:
        model = Resource
        fields = ['id', 'title', 'description', 'content_url', 'created_at', 'updated_at']
