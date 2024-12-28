from django.urls import path
from .views import ResourceListCreate

urlpatterns = [
    path('resources/', ResourceListCreate.as_view(), name='resource-list-create'),
]
