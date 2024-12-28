from django.urls import path
from .views import ResourceListCreate, ProtectedResourceView

urlpatterns = [
    # Path for listing all resources and creating a new resource (GET & POST)
    path('resources/', ResourceListCreate.as_view(), name='resource-list-create'),

    # Path for the protected resource, accessible only by authenticated users
    path('protected-resource/', ProtectedResourceView.as_view(), name='protected-resource'),
]
