from django.contrib import admin
from .models import Country,Flight,FlightBookinglog,FlightSeatManager
# Register your models here.

class CustomFlightAdmin(admin.ModelAdmin):
    """
        Customizes the Flight admin interface.

        Configures the display, filtering, searching, and ordering options for the Flight model
        in the Django admin interface. Additionally, provides read-only fields based on the object's state.

        Attributes:
            model: The Flight model to be managed by this admin class.
            list_display: The fields to be displayed in the list view of the admin interface.
            list_filter: The fields to be used for filtering in the admin interface.
            search_fields: The fields to be used for searching in the admin interface.
            ordering: The default ordering of records in the admin interface.
    """
    model = Flight
    list_display = ('number','name','source_name','destination_name','departure_date','departure_time','seats')
    list_filter = ('number','name','source__name','destination__name','departure_date','departure_time','seats')
   
    search_fields = ('number','name','source__name','destination__name','departure_date','departure_time','seats',)
    ordering = ('number','name','source__name','destination__name','departure_date','departure_time','seats',)

    def source_name(self, obj):
        """Returns the name of the source country for the flight."""    
        return obj.source.name

    def destination_name(self, obj):
        """Returns the name of the destination country for the flight."""
        return obj.destination.name
    
    def get_readonly_fields(self, request, obj=None):
        """
        Returns read-only fields based on the object's state.
        """
        if obj:
            return ('seats','cancellation_period')
        return ()
class CustomFlightSeatManagerAdmin(admin.ModelAdmin):
    """
    Customizes the FlightSeatManager admin interface.

    Configures the display, filtering, searching, and ordering options for the FlightSeatManager model
    in the Django admin interface. Additionally, provides read-only fields based on the object's state.

    Attributes:
        model: The FlightSeatManager model to be managed by this admin class.
        list_display: The fields to be displayed in the list view of the admin interface.
        list_filter: The fields to be used for filtering in the admin interface.
        search_fields: The fields to be used for searching in the admin interface.
        ordering: The default ordering of records in the admin interface.
    """
    
    model = FlightSeatManager
    list_display = ('flight_name','seat','status','created_at','modified_at')
    list_filter = ('flight__name','seat','status','created_at','modified_at')
   
    search_fields = ('flight__name','seat','status','created_at','modified_at')
    ordering = ('flight__name','seat','status','created_at','modified_at')

    def flight_name(self, obj):
        """Returns the name of the flight for the seat."""
        return obj.flight.name

    def get_readonly_fields(self, request, obj=None):
        """
        Returns read-only fields based on the object's state.
        """
        if obj:
            return ('flight','seat')
        return ()
    
    def has_add_permission(self, request):
        """
        Specifies whether to allow addition of new FlightSeatManager instances via the admin interface.
        """
        return False
class CustomFlightBookinglogAdmin(admin.ModelAdmin):
    """
    Customizes the FlightBookinglog admin interface.

    Configures the display, filtering, searching, and ordering options for the FlightBookinglog model
    in the Django admin interface. Additionally, provides read-only fields based on the object's state.

    Attributes:
        model: The FlightBookinglog model to be managed by this admin class.
        list_display: The fields to be displayed in the list view of the admin interface.
        list_filter: The fields to be used for filtering in the admin interface.
        search_fields: The fields to be used for searching in the admin interface.
        ordering: The default ordering of records in the admin interface.
    """
    
    model = FlightBookinglog
    list_display = ('user_name','user_email','flight_name','seat','status','created_at','modified_at')
    list_filter = ('user__name','user__email','flight__name','seat','status','created_at','modified_at')
   
    search_fields = ('user__name','user__email','flight__name','seat','status','created_at','modified_at')
    ordering = ('user__name','user__email','flight__name','seat','status','created_at','modified_at')

    def user_name(self, obj):
        """Returns the name of the user associated with the booking."""
        return obj.user.name
    
    def user_email(self, obj):
        """Returns the email of the user associated with the booking."""
        return obj.user.email
    
    def flight_name(self, obj):
        """Returns the name of the flight associated with the booking."""
        return obj.flight.name

    def has_add_permission(self, request):
        """
        Specifies whether to allow addition of new FlightBookinglog instances via the admin interface.
        """
        return False
    
    def get_readonly_fields(self, request, obj=None):
        """
        Returns read-only fields based on the object's state.
        """
        if obj:
            return ('flight','seat','user','status')
        return ()


admin.site.register(Country)

admin.site.register(Flight,CustomFlightAdmin)
admin.site.register(FlightSeatManager,CustomFlightSeatManagerAdmin)
admin.site.register(FlightBookinglog,CustomFlightBookinglogAdmin)