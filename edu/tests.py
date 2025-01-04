from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import UserProfile, ChildProfile, Resource, PhoneticsModule, MathModule, STEMModule
from django.contrib.auth.models import User

class APITestCase(TestCase):
    """
    Test case for API endpoints.
    """

    def setUp(self):
        """
        Set up test data and authenticated client.
        Runs before every test method.
        """
        # Create a test user and authenticate
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()
        self.client.login(username='testuser', password='password123')

        # Create test data for the models
        self.user_profile = UserProfile.objects.create(user=self.user, bio="Test bio")
        self.child_profile = ChildProfile.objects.create(user_profile=self.user_profile, name="Child 1", age=5)
        self.resource = Resource.objects.create(title="Test Resource", description="Resource Description", link="http://example.com")
        self.phonetics_module = PhoneticsModule.objects.create(title="Phonetics 101", description="Learn Phonetics")
        self.math_module = MathModule.objects.create(title="Math 101", description="Learn Math")
        self.stem_module = STEMModule.objects.create(title="STEM 101", description="Learn STEM")

    def test_user_profile_list(self):
        """
        Test listing all user profiles.
        Verifies the API returns the correct status code and includes the expected data.
        """
        response = self.client.get(reverse('userprofile-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test bio", str(response.data))  # Check if the response contains the bio

    def test_user_profile_creation(self):
        """
        Test creating a new user profile.
        Ensures a new profile is added to the database and the correct status code is returned.
        """
        data = {"bio": "Another bio"}
        response = self.client.post(reverse('userprofile-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 2)  # Confirm that the profile count increased

    def test_user_profile_detail(self):
        """
        Test retrieving details of a specific user profile.
        Confirms that the API returns the correct details for the given user profile.
        """
        response = self.client.get(reverse('userprofile-detail', args=[self.user_profile.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['bio'], "Test bio")  # Verify the bio matches the test data

    def test_child_profile_creation(self):
        """
        Test creating a child profile.
        Ensures the child profile is successfully added to the database.
        """
        data = {"user_profile": self.user_profile.id, "name": "Child 2", "age": 6}
        response = self.client.post(reverse('childprofile-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ChildProfile.objects.count(), 2)  # Confirm that the child profile count increased

    def test_resource_list(self):
        """
        Test listing all resources.
        Verifies the API returns the correct resources with the appropriate status code.
        """
        response = self.client.get(reverse('resource-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Resource", str(response.data))  # Check if the response contains the resource title

    def test_phonetics_module_creation(self):
        """
        Test creating a phonetics module.
        Ensures a new phonetics module is successfully added to the database.
        """
        data = {"title": "Phonetics 102", "description": "Advanced Phonetics"}
        response = self.client.post(reverse('phoneticsmodule-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PhoneticsModule.objects.count(), 2)  # Confirm that the phonetics module count increased

    def test_math_module_detail(self):
        """
        Test retrieving details of a specific math module.
        Verifies the API returns the correct data for the requested module.
        """
        response = self.client.get(reverse('mathmodule-detail', args=[self.math_module.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Math 101")  # Verify the title matches the test data

    def test_stem_module_update(self):
        """
        Test updating a STEM module.
        Confirms that the module's details are successfully updated in the database.
        """
        data = {"title": "Updated STEM 101", "description": "Updated STEM"}
        response = self.client.put(reverse('stemmule-detail', args=[self.stem_module.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(STEMModule.objects.get(id=self.stem_module.id).title, "Updated STEM 101")

    def test_unauthorized_access(self):
        """
        Test that unauthorized users cannot access the API.
        Confirms that the API blocks access for unauthenticated clients.
        """
        client = APIClient()  # Create an unauthenticated client
        response = client.get(reverse('userprofile-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Check for forbidden status code
