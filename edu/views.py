from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import UserProfile, ChildProfile, Resource, PhoneticsModule, MathModule, STEMModule
from .serializers import (
    UserProfileSerializer, 
    ChildProfileSerializer, 
    ResourceSerializer, 
    PhoneticsModuleSerializer, 
    MathModuleSerializer, 
    STEMModuleSerializer
)

# Base mixin for shared functionality
class BaseViewMixin:
    permission_classes = [permissions.IsAuthenticated]

    def handle_exception(self, exc):
        """
        Custom error response handler.
        """
        if isinstance(exc, NotFound):
            return Response({"error": "Resource not found."}, status=status.HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)

# Custom Pagination
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Custom Permissions
class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to allow only owners or admins to edit/delete objects.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user

# User Profile Views
class UserProfileListCreateView(BaseViewMixin, generics.ListCreateAPIView):
    """
    API endpoint to list and create user profiles.
    - `GET`: Retrieve a list of user profiles.
    - `POST`: Create a new user profile linked to the authenticated user.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        """
        Save the user profile associated with the authenticated user.
        """
        try:
            serializer.save(user=self.request.user)
        except Exception as e:
            raise ValidationError({"error": f"Failed to create user profile: {str(e)}"})

class UserProfileDetailView(BaseViewMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, and delete a user profile.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = BaseViewMixin.permission_classes + [IsOwnerOrAdmin]

# Child Profile Views
class ChildProfileListCreateView(BaseViewMixin, generics.ListCreateAPIView):
    """
    API endpoint to list and create child profiles.
    """
    queryset = ChildProfile.objects.all()
    serializer_class = ChildProfileSerializer
    pagination_class = CustomPagination

class ChildProfileDetailView(BaseViewMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, and delete a child profile.
    """
    queryset = ChildProfile.objects.all()
    serializer_class = ChildProfileSerializer
    permission_classes = BaseViewMixin.permission_classes + [IsOwnerOrAdmin]

# Resource Views
class ResourceListCreateView(BaseViewMixin, generics.ListCreateAPIView):
    """
    API endpoint to list and create educational resources.
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'level']

class ResourceDetailView(BaseViewMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, and delete a specific resource.
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = BaseViewMixin.permission_classes + [IsOwnerOrAdmin]

# Phonetics Module Views
class PhoneticsModuleListCreateView(BaseViewMixin, generics.ListCreateAPIView):
    """
    API endpoint to list and create phonetics modules.
    """
    queryset = PhoneticsModule.objects.all()
    serializer_class = PhoneticsModuleSerializer
    pagination_class = CustomPagination

class PhoneticsModuleDetailView(BaseViewMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, and delete a phonetics module.
    """
    queryset = PhoneticsModule.objects.all()
    serializer_class = PhoneticsModuleSerializer
    permission_classes = BaseViewMixin.permission_classes + [IsOwnerOrAdmin]

# Math Module Views
class MathModuleListCreateView(BaseViewMixin, generics.ListCreateAPIView):
    """
    API endpoint to list and create math modules.
    """
    queryset = MathModule.objects.all()
    serializer_class = MathModuleSerializer
    pagination_class = CustomPagination

class MathModuleDetailView(BaseViewMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, and delete a math module.
    """
    queryset = MathModule.objects.all()
    serializer_class = MathModuleSerializer
    permission_classes = BaseViewMixin.permission_classes + [IsOwnerOrAdmin]

# STEM Module Views
class STEMModuleListCreateView(BaseViewMixin, generics.ListCreateAPIView):
    """
    API endpoint to list and create STEM modules.
    """
    queryset = STEMModule.objects.all()
    serializer_class = STEMModuleSerializer
    pagination_class = CustomPagination

class STEMModuleDetailView(BaseViewMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, and delete a STEM module.
    """
    queryset = STEMModule.objects.all()
    serializer_class = STEMModuleSerializer
    permission_classes = BaseViewMixin.permission_classes + [IsOwnerOrAdmin]

