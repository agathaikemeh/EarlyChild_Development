from django.urls import path
from . import views

# Define URL patterns for the educational app
urlpatterns = [
    # User Profile Endpoints
    path(
        'user-profiles/', 
        views.UserProfileListCreateView.as_view(), 
        name='user-profile-list-create'
    ),  # Endpoint for listing and creating user profiles
    path(
        'user-profiles/<int:pk>/', 
        views.UserProfileDetailView.as_view(), 
        name='user-profile-detail'
    ),  # Endpoint for retrieving, updating, and deleting a specific user profile

    # Child Profile Endpoints
    path(
        'child-profiles/', 
        views.ChildProfileListCreateView.as_view(), 
        name='child-profile-list-create'
    ),  # Endpoint for listing and creating child profiles
    path(
        'child-profiles/<int:pk>/', 
        views.ChildProfileDetailView.as_view(), 
        name='child-profile-detail'
    ),  # Endpoint for retrieving, updating, and deleting a specific child profile

    # Resource Endpoints
    path(
        'resources/', 
        views.ResourceListCreateView.as_view(), 
        name='resource-list-create'
    ),  # Endpoint for listing and creating resources
    path(
        'resources/<int:pk>/', 
        views.ResourceDetailView.as_view(), 
        name='resource-detail'
    ),  # Endpoint for retrieving, updating, and deleting a specific resource

    # Phonetics Module Endpoints
    path(
        'phonetics-modules/', 
        views.PhoneticsModuleListCreateView.as_view(), 
        name='phonetics-module-list-create'
    ),  # Endpoint for listing and creating phonetics modules
    path(
        'phonetics-modules/<int:pk>/', 
        views.PhoneticsModuleDetailView.as_view(), 
        name='phonetics-module-detail'
    ),  # Endpoint for retrieving, updating, and deleting a specific phonetics module

    # Math Module Endpoints
    path(
        'math-modules/', 
        views.MathModuleListCreateView.as_view(), 
        name='math-module-list-create'
    ),  # Endpoint for listing and creating math modules
    path(
        'math-modules/<int:pk>/', 
        views.MathModuleDetailView.as_view(), 
        name='math-module-detail'
    ),  # Endpoint for retrieving, updating, and deleting a specific math module

    # STEM Module Endpoints
    path(
        'stem-modules/', 
        views.STEMModuleListCreateView.as_view(), 
        name='stem-module-list-create'
    ),  # Endpoint for listing and creating STEM modules
    path(
        'stem-modules/<int:pk>/', 
        views.STEMModuleDetailView.as_view(), 
        name='stem-module-detail'
    ),  # Endpoint for retrieving, updating, and deleting a specific STEM module
]

