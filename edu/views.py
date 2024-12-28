
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Resource
from .serializers import ResourceSerializer

class ResourceListCreate(APIView):
    """
    Handle listing all resources (GET) and creating a new resource (POST).
    """
    def get(self, request):
        resources = Resource.objects.all()  # Fetch all resources
        serializer = ResourceSerializer(resources, many=True)  # Serialize the data
        return Response(serializer.data)  # Return JSON response

    def post(self, request):
        serializer = ResourceSerializer(data=request.data)  # Deserialize input data
        if serializer.is_valid():  # Validate data
            serializer.save()  # Save the new resource
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


