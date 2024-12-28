from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import logging
from .models import Resource
from .serializers import ResourceSerializer

# Setup logging
logger = logging.getLogger(__name__)

class ResourceListCreate(APIView):
    """
    Handle listing all resources (GET) and creating a new resource (POST).
    """
    def get(self, request):
        """
        Handles GET requests to fetch all resources.

        Args:
            request: The incoming HTTP request.

        Returns:
            Response: A JSON response with serialized resource data.
        """
        # Log the user making the request (if authenticated)
        user = request.user if request.user.is_authenticated else "Anonymous"
        logger.info(f"GET request received by {user}")

        resources = Resource.objects.all()  # Fetch all resources
        serializer = ResourceSerializer(resources, many=True)  # Serialize the data
        return Response(serializer.data)  # Return JSON response

    def post(self, request):
        """
        Handles POST requests to create a new resource.

        Args:
            request: The incoming HTTP request with the data.

        Returns:
            Response: A JSON response with the created resource data or errors.
        """
        # Log the user making the request (if authenticated)
        user = request.user if request.user.is_authenticated else "Anonymous"
        logger.info(f"POST request received by {user} with data: {request.data}")

        serializer = ResourceSerializer(data=request.data)  # Deserialize input data
        if serializer.is_valid():  # Validate data
            serializer.save()  # Save the new resource
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProtectedResourceView(APIView):
    """
    Example of a protected API endpoint.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]  # Ensure TokenAuthentication is used

    def get(self, request):
        """
        Handles GET requests to return a protected message.

        Args:
            request: The incoming HTTP request.

        Returns:
            Response: A JSON response with a protected message.
        """
        # Log the authenticated user making the request
        user = request.user
        logger.info(f"Protected resource accessed by {user.username}")

        return Response({"message": f"This is a protected resource, accessed by {user.username}."})
