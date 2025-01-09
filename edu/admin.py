from django.contrib import admin
from .models import UserProfile, ChildProfile, Resource, PhoneticsModule, MathModule, STEMModule

# Admin registration with customization for UserProfile model
class ChildProfileInline(admin.TabularInline):
    """
    Inline view for managing children directly from the UserProfile admin.
    """
    model = ChildProfile
    extra = 1  # Number of blank forms shown for adding children


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Custom admin view for UserProfile model.
    """
    list_display = ('id', 'username', 'email', 'role', 'created_at', 'updated_at')  # Columns to show in admin
    search_fields = ('username', 'email')  # Enable search by username or email
    list_filter = ('role', 'created_at', 'updated_at')  # Add filter options
    inlines = [ChildProfileInline]  # Inline editing for child profiles
    ordering = ('-created_at',)  # Order by creation date


# Admin registration with customization for ChildProfile model
@admin.register(ChildProfile)
class ChildProfileAdmin(admin.ModelAdmin):
    """
    Custom admin view for ChildProfile model.
    """
    list_display = ('id', 'user', 'name', 'age', 'created_at', 'updated_at')  # Fields to display in admin
    search_fields = ('name',)  # Enable search by child's name
    list_filter = ('age', 'created_at', 'updated_at')  # Add filter options
    ordering = ('-created_at',)  # Order by creation date
    raw_id_fields = ('user',)  # Optimize foreign key field


# Admin registration for Resource model
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    """
    Custom admin view for Resource model.
    """
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at')  # Fields to display
    search_fields = ('title', 'description')  # Enable search by title or description
    list_filter = ('created_at', 'updated_at')  # Add filter options
    ordering = ('-created_at',)  # Order by creation date


# Admin registration for PhoneticsModule model
@admin.register(PhoneticsModule)
class PhoneticsModuleAdmin(admin.ModelAdmin):
    """
    Custom admin view for PhoneticsModule model.
    """
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at')  # Fields to display
    search_fields = ('title', 'description')  # Enable search by title or description
    list_filter = ('created_at', 'updated_at')  # Add filter options
    filter_horizontal = ('resources',)  # For many-to-many fields
    ordering = ('-created_at',)  # Order by creation date


# Admin registration for MathModule model
@admin.register(MathModule)
class MathModuleAdmin(admin.ModelAdmin):
    """
    Custom admin view for MathModule model.
    """
    list_display = ('id', 'title', 'difficulty_level', 'created_at', 'updated_at')  # Fields to display
    search_fields = ('title', 'description')  # Enable search by title or description
    list_filter = ('difficulty_level', 'created_at', 'updated_at')  # Add filter options
    filter_horizontal = ('resources',)  # For many-to-many fields
    ordering = ('-created_at',)  # Order by creation date


# Admin registration for STEMModule model
@admin.register(STEMModule)
class STEMModuleAdmin(admin.ModelAdmin):
    """
    Custom admin view for STEMModule model.
    """
    list_display = ('id', 'title', 'video_url', 'created_at', 'updated_at')  # Fields to display
    search_fields = ('title', 'description', 'video_url')  # Enable search by title, description, or video URL
    list_filter = ('created_at', 'updated_at')  # Add filter options
    filter_horizontal = ('resources',)  # For many-to-many fields
    ordering = ('-created_at',)  # Order by creation date


