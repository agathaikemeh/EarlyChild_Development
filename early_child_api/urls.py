from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static

def homepage(request):
    """
    A simple homepage view that returns a JSON response.
    """
    return JsonResponse({
        "message": "Welcome to the Early Child API. Go to /api/ to interact with the API."
    })

urlpatterns = [
    path('', homepage),  # Root path
    path('admin/', admin.site.urls),  # Admin dashboard
    path('api/', include('edu.urls')),  # Include URLs for the 'edu' app
    # Add other app URLs here
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Add custom error handlers if desired
# handler404 = 'my_project.views.custom_404'
# handler500 = 'my_project.views.custom_500'

