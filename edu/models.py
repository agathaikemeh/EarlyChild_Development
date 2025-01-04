from django.db import models

# User Profile Models
class UserProfile(models.Model):
    """
    Model to represent user profiles (Parent, Teacher, or Admin).
    """
    ROLE_CHOICES = [
        ('parent', 'Parent'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]
    username = models.CharField(max_length=100)  # Username for the user
    email = models.EmailField(unique=True)      # Email of the user
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)  # Role of the user
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set at creation
    updated_at = models.DateTimeField(auto_now=True)      # Auto-update on save

    def __str__(self):
        return self.username

# Child Profile Model
class ChildProfile(models.Model):
    """
    Model to represent child profiles for tracking learning progress.
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="children")  # Parent/Teacher link
    name = models.CharField(max_length=100)  # Child's name
    age = models.PositiveIntegerField()      # Child's age
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set at creation
    updated_at = models.DateTimeField(auto_now=True)      # Auto-update on save

    def __str__(self):
        return self.name

# Educational Resource Model
class Resource(models.Model):
    """
    Model to define an educational resource (e.g., videos, documents).
    """
    title = models.CharField(max_length=255)  # Title of the resource
    description = models.TextField()          # Detailed description of the resource
    content_url = models.URLField()           # Link to the resource content
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set at creation
    updated_at = models.DateTimeField(auto_now=True)      # Auto-update on save

    def __str__(self):
        return self.title

# Phonetics Module Model
class PhoneticsModule(models.Model):
    """
    Model for phonetics learning modules, including sounds and pronunciation.
    """
    title = models.CharField(max_length=255)  # Title of the phonetics module
    description = models.TextField()          # Description of the module
    audio_file = models.FileField(upload_to='phonetics_audio/')  # Audio file for learning
    resources = models.ManyToManyField(Resource, blank=True)  # Related educational resources
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set at creation
    updated_at = models.DateTimeField(auto_now=True)      # Auto-update on save

    def __str__(self):
        return self.title

# Mathematics Module Model
class MathModule(models.Model):
    """
    Model for mathematics learning modules, including games and problem-solving.
    """
    title = models.CharField(max_length=255)  # Title of the math module
    description = models.TextField()          # Description of the module
    difficulty_level = models.CharField(max_length=50, default="Easy")  # Difficulty level
    resources = models.ManyToManyField(Resource, blank=True)  # Related educational resources
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set at creation
    updated_at = models.DateTimeField(auto_now=True)      # Auto-update on save

    def __str__(self):
        return self.title

# STEM Module Model
class STEMModule(models.Model):
    """
    Model for STEM learning modules, including science, technology, and experiments.
    """
    title = models.CharField(max_length=255)  # Title of the STEM module
    description = models.TextField()          # Description of the module
    video_url = models.URLField(blank=True, null=True)  # Link to related videos
    resources = models.ManyToManyField(Resource, blank=True)  # Related educational resources
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set at creation
    updated_at = models.DateTimeField(auto_now=True)      # Auto-update on save

    def __str__(self):
        return self.title


