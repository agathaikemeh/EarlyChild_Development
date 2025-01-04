from rest_framework import serializers
from .models import UserProfile, ChildProfile, Resource, PhoneticsModule, MathModule, STEMModule

# Serializer for UserProfile
class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserProfile model.
    Handles serialization and deserialization of user profile data.
    """
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'role', 'created_at', 'updated_at']  # Fields to include in the serialized output

# Serializer for ChildProfile
class ChildProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the ChildProfile model.
    Provides nested user details using the UserProfileSerializer.
    """
    user = UserProfileSerializer(read_only=True)  # Nested UserProfile serializer for displaying associated user information

    class Meta:
        model = ChildProfile
        fields = ['id', 'user', 'name', 'age', 'created_at', 'updated_at']  # Fields to include in the serialized output

# Serializer for Resource
class ResourceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Resource model.
    Handles educational resources like videos, articles, or games.
    """
    class Meta:
        model = Resource
        fields = ['id', 'title', 'description', 'content_url', 'created_at', 'updated_at']  # Fields to include in the serialized output

# Serializer for PhoneticsModule
class PhoneticsModuleSerializer(serializers.ModelSerializer):
    """
    Serializer for the PhoneticsModule model.
    Includes nested resources for detailed information about associated educational content.
    """
    resources = ResourceSerializer(many=True, read_only=True)  # Nested Resource serializer to display related resources

    class Meta:
        model = PhoneticsModule
        fields = ['id', 'title', 'description', 'audio_file', 'resources', 'created_at', 'updated_at']  # Fields to include in the serialized output

# Serializer for MathModule
class MathModuleSerializer(serializers.ModelSerializer):
    """
    Serializer for the MathModule model.
    Includes nested resources for detailed information about associated educational content.
    """
    resources = ResourceSerializer(many=True, read_only=True)  # Nested Resource serializer to display related resources

    class Meta:
        model = MathModule
        fields = ['id', 'title', 'description', 'difficulty_level', 'resources', 'created_at', 'updated_at']  # Fields to include in the serialized output

# Serializer for STEMModule
class STEMModuleSerializer(serializers.ModelSerializer):
    """
    Serializer for the STEMModule model.
    Includes nested resources for detailed information about associated educational content.
    """
    resources = ResourceSerializer(many=True, read_only=True)  # Nested Resource serializer to display related resources

    class Meta:
        model = STEMModule
        fields = ['id', 'title', 'description', 'video_url', 'resources', 'created_at', 'updated_at']  # Fields to include in the serialized output
