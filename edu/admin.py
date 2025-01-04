from django.contrib import admin
from .models import UserProfile, ChildProfile, Resource, PhoneticsModule, MathModule, STEMModule

# Admin registration with customization for UserProfile model
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Custom admin view for UserProfile model.
    Allows admin to manage user profiles with specific fields displayed.
    """
    list_display = ('id', 'username', 'email', 'role', 'created_at', 'updated_at')  # Columns to show in admin
    search_fields = ('username',)  # Enable search by username
    list_filter = ('role', 'created_at', 'updated_at')  # Add filter options by role and date

# Admin registration with customization for ChildProfile model
@admin.register(ChildProfile)
class ChildProfileAdmin(admin.ModelAdmin):
    """
    Custom admin view for ChildProfile model.
    """
    list_display = ('id', 'user', 'name', 'age')  # Fields to display in admin
    search_fields = ('name',)  # Enable search by child's name
    list_filter = ('age',)  # Add filter option by age

# Admin registration for Resource model
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    """
    Custom admin view for Resource model.
    """
    list_display = ('id', 'title', 'created_at')  # Fields to display
    search_fields = ('title',)  # Enable search by title
    list_filter = ('created_at',)  # Add filter options by date

# Admin registration for PhoneticsModule model
@admin.register(PhoneticsModule)
class PhoneticsModuleAdmin(admin.ModelAdmin):
    """
    Custom admin view for PhoneticsModule model.
    """
    list_display = ('id', 'title', 'description')  # Fields to display
    search_fields = ('title',)  # Enable search by title

# Admin registration for MathModule model
@admin.register(MathModule)
class MathModuleAdmin(admin.ModelAdmin):
    """
    Custom admin view for MathModule model.
    """
    list_display = ('id', 'title', 'difficulty_level')  # Fields to display
    search_fields = ('title',)  # Enable search by title

# Admin registration for STEMModule model
@admin.register(STEMModule)
class STEMModuleAdmin(admin.ModelAdmin):
    """
    Custom admin view for STEMModule model.
    """
    list_display = ('id', 'title', 'created_at')  # Fields to display
    search_fields = ('title',)  # Enable search by title
    list_filter = ('created_at',)  # Add filter options

