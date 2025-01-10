from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views  # Import the auth token view

def homepage(request):
    """
    A simple homepage view that returns a JSON response.
    """
    return JsonResponse({
        "message": "Welcome to the Early Child API. Navigate to /api/ for API endpoints.",
        "available_endpoints": {
            "user_profiles": "/api/v1/user-profiles/",
            "child_profiles": "/api/v1/child-profiles/",
            "resources": "/api/v1/resources/",
            "phonetics_modules": "/api/v1/phonetics-modules/",
            "math_modules": "/api/v1/math-modules/",
            "stem_modules": "/api/v1/stem-modules/",
            "auth_token": "/api/v1/auth-token/",  # Add auth token endpoint
        }
    })

urlpatterns = [
    path('', homepage),  # Root path for homepage
    path('admin/', admin.site.urls),  # Admin dashboard
    path('api/', include('edu.urls', namespace='edu')),  # Include 'edu' app URLs with namespace
    path('api/v1/auth-token/', views.obtain_auth_token, name='api-token-auth'),  # Authentication endpoint
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
