from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    """
    Customizes the User admin interface.

    Configures the display, filtering, and ordering options for the User model
    in the Django admin interface. Additionally, specifies fieldsets for adding
    and editing users.

    Attributes:
        model: The User model to be managed by this admin class.
        list_display: The fields to be displayed in the list view of the admin interface.
        list_filter: The fields to be used for filtering in the admin interface.
        fieldsets: The sets of fields to be displayed on the add and change forms in the admin interface.
        add_fieldsets: The sets of fields to be displayed on the add form in the admin interface.
        search_fields: The fields to be used for searching in the admin interface.
        ordering: The default ordering of records in the admin interface.
    """
     
    model = User
    list_display = ('email','name','created_at','is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('name','email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
   
    search_fields = ('email',)
    ordering = ('email',)
admin.site.register(User, CustomUserAdmin)