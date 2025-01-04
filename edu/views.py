from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import UserProfile, ChildProfile, Resource, PhoneticsModule, MathModule, STEMModule
from .serializers import (
    UserProfileSerializer, 
    ChildProfileSerializer, 
    ResourceSerializer, 
    PhoneticsModuleSerializer, 
    MathModuleSerializer, 
    STEMModuleSerializer
)

# Base mixin for shared functionality and error handling
class BaseViewMixin:
    def handle_exception(self, exc):
        """
        Custom error response handler.
        """
        if isinstance(exc, NotFound):
            return Response({"error": "Resource not found."}, status=status.HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)

# User Profile Views
class UserProfileListCreateView(BaseViewMixin, generics.ListCreateAPIView):
    """
    API view for listing and creating user profiles.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the user profile associated with the authenticated user.
        """
        try:
            serializer.save(user=self.request.user)
        except Exception as e:
            return Response(
                {"error": f"Failed to create user profile: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

class UserProfileDetailView(BaseViewMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a user profile.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Override to handle the case where a user profile does not exist.
        """
        try:
            return super().get_object()
        except UserProfile.DoesNotExist:
            raise NotFound("The requested user profile does not exist.")

# Child Profile Views
class ChildProfileListCreateView(BaseViewMixin, generics.ListCreateAPIView):
    """
    API view for listing and creating child profiles.
    """
    queryset = ChildProfile.objects.all()
    serializer_class = ChildProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class ChildProfileDetailView(BaseViewMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a child profile.
    """
    queryset = ChildProfile.objects.all()
    serializer_class = ChildProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

# Resource Views
class ResourceListCreateView(BaseViewMixin, generics.ListCreateAPIView):
    """
    API view for listing and creating educational resources.
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

class ResourceDetailView(BaseViewMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific resource.
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

# Phonetics Module Views
class PhoneticsModuleListCreateView(BaseViewMixin, generics.ListCreateAPIView):
    """
    API view for listing and creating phonetics modules.
    """
    queryset = PhoneticsModule.objects.all()
    serializer_class = PhoneticsModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

class PhoneticsModuleDetailView(BaseViewMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a phonetics module.
    """
    queryset = PhoneticsModule.objects.all()
    serializer_class = PhoneticsModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

# Math Module Views
class MathModuleListCreateView(BaseViewMixin, generics.ListCreateAPIView):
    """
    API view for listing and creating math modules.
    """
    queryset = MathModule.objects.all()
    serializer_class = MathModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

class MathModuleDetailView(BaseViewMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a math module.
    """
    queryset = MathModule.objects.all()
    serializer_class = MathModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

# STEM Module Views
class STEMModuleListCreateView(BaseViewMixin, generics.ListCreateAPIView):
    """
    API view for listing and creating STEM modules.
    """
    queryset = STEMModule.objects.all()
    serializer_class = STEMModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

class STEMModuleDetailView(BaseViewMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a STEM module.
    """
    queryset = STEMModule.objects.all()
    serializer_class = STEMModuleSerializer
    permission_classes = [permissions.IsAuthenticated]
