from django.db import models

class Resource(models.Model):
    """
    Model to define an educational resource.
    """
    title = models.CharField(max_length=255)  # Title of the resource
    description = models.TextField()          # Detailed description
    content_url = models.URLField()           # Link to the resource content
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set at creation
    updated_at = models.DateTimeField(auto_now=True)      # Auto-update on save

    def __str__(self):
        return self.title  # Display the title in admin and debugging


