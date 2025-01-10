from django.urls import path
from . import views

app_name = 'edu'  # Namespace for this app

urlpatterns = [
    # User Profile Endpoints
    path(
        'v1/user-profiles/',
        views.UserProfileListCreateView.as_view(),
        name='user-profiles-list'
    ),
    path(
        'v1/user-profiles/<int:pk>/',
        views.UserProfileDetailView.as_view(),
        name='user-profile-detail'
    ),

    # Child Profile Endpoints
    path(
        'v1/child-profiles/',
        views.ChildProfileListCreateView.as_view(),
        name='child-profiles-list'
    ),
    path(
        'v1/child-profiles/<int:pk>/',
        views.ChildProfileDetailView.as_view(),
        name='child-profile-detail'
    ),

    # Resource Endpoints
    path(
        'v1/resources/',
        views.ResourceListCreateView.as_view(),
        name='resources-list'
    ),
    path(
        'v1/resources/<int:pk>/',
        views.ResourceDetailView.as_view(),
        name='resource-detail'
    ),

    # Phonetics Module Endpoints
    path(
        'v1/phonetics-modules/',
        views.PhoneticsModuleListCreateView.as_view(),
        name='phonetics-modules-list'
    ),
    path(
        'v1/phonetics-modules/<int:pk>/',
        views.PhoneticsModuleDetailView.as_view(),
        name='phonetics-module-detail'
    ),

    # Math Module Endpoints
    path(
        'v1/math-modules/',
        views.MathModuleListCreateView.as_view(),
        name='math-modules-list'
    ),
    path(
        'v1/math-modules/<int:pk>/',
        views.MathModuleDetailView.as_view(),
        name='math-module-detail'
    ),

    # STEM Module Endpoints
    path(
        'v1/stem-modules/',
        views.STEMModuleListCreateView.as_view(),
        name='stem-modules-list'
    ),
    path(
        'v1/stem-modules/<int:pk>/',
        views.STEMModuleDetailView.as_view(),
        name='stem-module-detail'
    ),
]


