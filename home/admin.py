from django.contrib import admin
from .models import Userlog
# Register your models here.
class CustomUserlogAdmin(admin.ModelAdmin):
    """
        Customizes the Userlog admin interface.

        Configures the display, filtering, searching, and ordering options for the Userlog model
        in the Django admin interface. Additionally, provides read-only fields based on the object's state.

        Attributes:
            model: The Userlog model to be managed by this admin class.
            list_display: The fields to be displayed in the list view of the admin interface.
            list_filter: The fields to be used for filtering in the admin interface.
            search_fields: The fields to be used for searching in the admin interface.
            ordering: The default ordering of records in the admin interface.
    """
    model = Userlog
    list_display = ('user_name','user_email','flight_name','seat','status','created_at','modified_at')
    list_filter = ('user__name','user__email','flight__name','seat','status','created_at','modified_at')
   
    search_fields = ('user__name','user__email','flight__name','seat','status','created_at','modified_at')
    ordering = ('user__name','user__email','flight__name','seat','status','created_at','modified_at')

    def user_name(self, obj):
        return obj.user.name
    
    def user_email(self, obj):
        return obj.user.email
    
    def flight_name(self, obj):
        return obj.flight.name

    
    def get_readonly_fields(self, request, obj=None):
        """
            Returns read-only fields based on the object's state.

            If the object exists (i.e., during editing), returns 'flight', 'seat', 'user', 'is_changed', and 'remarks'
            as read-only fields. Otherwise, returns an empty tuple indicating no read-only fields.
        """

        if obj:
            return ('flight','seat','user','is_changed','remarks')
        return ()

admin.site.register(Userlog,CustomUserlogAdmin)
