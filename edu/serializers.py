from rest_framework import serializers
from .models import UserProfile, ChildProfile, Resource, PhoneticsModule, MathModule, STEMModule


# Serializer for UserProfile
class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserProfile model.
    Handles serialization and validation of user profile data.
    """

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'role', 'created_at', 'updated_at']

    def validate_email(self, value):
        """
        Validate that the email is in the correct format and unique.
        """
        if UserProfile.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate_username(self, value):
        """
        Validate that the username is unique.
        """
        if UserProfile.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def validate_role(self, value):
        """
        Validate that the role is one of the predefined choices.
        """
        valid_roles = [choice[0] for choice in UserProfile.ROLE_CHOICES]
        if value not in valid_roles:
            raise serializers.ValidationError(f"Invalid role. Valid roles are: {', '.join(valid_roles)}.")
        return value

    def create(self, validated_data):
        """
        Override the create method to handle the creation of a UserProfile.
        """
        user_profile = UserProfile.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role'],
        )
        return user_profile


# Serializer for ChildProfile
class ChildProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the ChildProfile model.
    Provides nested user details using the UserProfileSerializer.
    """
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = ChildProfile
        fields = ['id', 'user', 'name', 'age', 'created_at', 'updated_at']

    def create(self, validated_data):
        """
        Override the create method to handle the creation of a ChildProfile.
        """
        # Extract the user from the context
        user = self.context.get('user')
        if not user:
            raise serializers.ValidationError("User must be provided.")
        
        # Create the child profile with the provided user and validated data
        return ChildProfile.objects.create(user=user, **validated_data)


# Serializer for Resource
class ResourceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Resource model.
    Handles educational resources like videos, articles, or games.
    """

    class Meta:
        model = Resource
        fields = ['id', 'title', 'description', 'content_url', 'created_at', 'updated_at']

    def validate_content_url(self, value):
        """
        Validate that the content URL is a valid web address.
        """
        if not value.startswith(('http://', 'https://')):
            raise serializers.ValidationError("Content URL must start with 'http://' or 'https://'.")
        return value


# Serializer for PhoneticsModule
class PhoneticsModuleSerializer(serializers.ModelSerializer):
    """
    Serializer for the PhoneticsModule model.
    Includes nested resources for detailed information about associated educational content.
    """
    resources = ResourceSerializer(many=True, read_only=True)

    class Meta:
        model = PhoneticsModule
        fields = ['id', 'title', 'description', 'audio_file', 'resources', 'created_at', 'updated_at']

    def validate_title(self, value):
        """
        Validate the title for a phonetics module.
        """
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value


# Serializer for MathModule
class MathModuleSerializer(serializers.ModelSerializer):
    """
    Serializer for the MathModule model.
    Includes nested resources for detailed information about associated educational content.
    """
    resources = ResourceSerializer(many=True, read_only=True)

    class Meta:
        model = MathModule
        fields = ['id', 'title', 'description', 'difficulty_level', 'resources', 'created_at', 'updated_at']

    def validate_difficulty_level(self, value):
        """
        Validate the difficulty level is within an acceptable range (e.g., 1 to 5).
        """
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Difficulty level must be between 1 and 5.")
        return value


# Serializer for STEMModule
class STEMModuleSerializer(serializers.ModelSerializer):
    """
    Serializer for the STEMModule model.
    Includes nested resources for detailed information about associated educational content.
    """
    resources = ResourceSerializer(many=True, read_only=True)

    class Meta:
        model = STEMModule
        fields = ['id', 'title', 'description', 'video_url', 'resources', 'created_at', 'updated_at']

    def validate_video_url(self, value):
        """
        Validate that the video URL is a valid YouTube or other video platform URL.
        """
        if not value.startswith(('http://', 'https://')):
            raise serializers.ValidationError("Video URL must start with 'http://' or 'https://'.")
        return value
