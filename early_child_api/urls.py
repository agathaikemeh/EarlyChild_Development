from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def homepage(request):
    """
    A simple homepage view that returns a JSON response.
    This view will show a welcome message when visiting the root URL.
    """
    return JsonResponse({
        "message": "Welcome to the Early Child API. Go to /api/ to interact with the API."
    })

urlpatterns = [
    path('', homepage),  # Root path that returns a JSON response with a welcome message.
    path('admin/', admin.site.urls),  # Admin dashboard path.

    # Include URLs for the 'edu' app.
    path('api/', include('edu.urls')),  

    # Example: Other apps can also be included here in a similar manner.
]

# Comments:
# 1. The `homepage` function serves as a quick welcome response for the root URL.
# 2. `path('admin/', admin.site.urls)` is the built-in admin site.
# 3. `path('api/', include('edu.urls'))` directs API-related requests to the `edu` app.
# 4. Additional apps or functionalities can be added as needed using `path()` or `include()`.

