from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Simple homepage view that returns a JSON response
def homepage(request):
    """
    A simple homepage view that returns a JSON response.
    This view will show a welcome message when visiting the root URL.
    """
    return JsonResponse({
        "message": "Welcome to the Early Child API. Go to /api/resources/ to interact with the API."
    })

# URL patterns for the project
urlpatterns = [
    path('', homepage),  # Root path returns a JSON message (homepage)
    path('admin/', admin.site.urls),  # Admin URL for the Django admin panel
    path('api/', include('edu.urls')),  # Include URLs from the 'edu' app (where API endpoints are defined)
]
