from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import UserProfile, ChildProfile, Resource, PhoneticsModule, MathModule, STEMModule


class UserProfileTests(TestCase):
    def setUp(self):
        """
        Set up test data and authenticated client.
        Runs before every test method.
        """
        # Create a test user and authenticate
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()
        self.client.login(username='testuser', password='password123')

        # Create test data for various models
        self.user_profile = UserProfile.objects.create(username="testuser", email="testuser@example.com", role="parent")
        self.child_profile = ChildProfile.objects.create(user=self.user_profile, name="Child 1", age=5)
        self.resource = Resource.objects.create(title="Test Resource", description="Resource Description", content_url="http://example.com")
        self.phonetics_module = PhoneticsModule.objects.create(title="Phonetics 101", description="Learn Phonetics", audio_file=None)
        self.math_module = MathModule.objects.create(title="Math 101", description="Learn Math", difficulty_level="Easy")
        self.stem_module = STEMModule.objects.create(title="STEM 101", description="Learn STEM")

    def test_user_profile_creation(self):
        """
        Test the creation of a user profile.
        """
        self.assertEqual(self.user_profile.username, 'testuser')
        self.assertEqual(self.user_profile.email, 'testuser@example.com')
        self.assertEqual(self.user_profile.role, 'parent')

    def test_child_profile_creation(self):
        """
        Test the creation of a child profile linked to a user.
        """
        self.assertEqual(self.child_profile.name, 'Child 1')
        self.assertEqual(self.child_profile.age, 5)
        self.assertEqual(self.child_profile.user.username, 'testuser')

    def test_resource_creation(self):
        """
        Test the creation of an educational resource.
        """
        self.assertEqual(self.resource.title, 'Test Resource')
        self.assertEqual(self.resource.description, 'Resource Description')
        self.assertEqual(self.resource.content_url, 'http://example.com')

    def test_phonetics_module_creation(self):
        """
        Test the creation of a phonetics learning module.
        """
        self.assertEqual(self.phonetics_module.title, 'Phonetics 101')
        self.assertEqual(self.phonetics_module.description, 'Learn Phonetics')
        self.assertFalse(self.phonetics_module.audio_file)  # Updated assertion to check for empty file

    def test_math_module_creation(self):
        """
        Test the creation of a mathematics learning module.
        """
        self.assertEqual(self.math_module.title, 'Math 101')
        self.assertEqual(self.math_module.description, 'Learn Math')
        self.assertEqual(self.math_module.difficulty_level, 'Easy')

    def test_stem_module_creation(self):
        """
        Test the creation of a STEM learning module.
        """
        self.assertEqual(self.stem_module.title, 'STEM 101')
        self.assertEqual(self.stem_module.description, 'Learn STEM')

    def test_user_profile_str_method(self):
        """
        Test the __str__ method of the UserProfile model.
        """
        self.assertEqual(str(self.user_profile), 'testuser')

    def test_child_profile_str_method(self):
        """
        Test the __str__ method of the ChildProfile model.
        """
        self.assertEqual(str(self.child_profile), 'Child 1')

    def test_resource_str_method(self):
        """
        Test the __str__ method of the Resource model.
        """
        self.assertEqual(str(self.resource), 'Test Resource')

    def test_math_module_str_method(self):
        """
        Test the __str__ method of the MathModule model.
        """
        self.assertEqual(str(self.math_module), 'Math 101')

    def test_stem_module_str_method(self):
        """
        Test the __str__ method of the STEMModule model.
        """
        self.assertEqual(str(self.stem_module), 'STEM 101')



