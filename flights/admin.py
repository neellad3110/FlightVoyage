from django.contrib import admin
from .models import Country,Flight,FlightBookinglog,FlightSeatManager
# Register your models here.

class CustomFlightAdmin(admin.ModelAdmin):
    
    model = Flight
    list_display = ('number','name','source_name','destination_name','departure_date','departure_time','seats')
    list_filter = ('number','name','source__name','destination__name','departure_date','departure_time','seats')
   
    search_fields = ('number','name','source__name','destination__name','departure_date','departure_time','seats',)
    ordering = ('number','name','source__name','destination__name','departure_date','departure_time','seats',)

    def source_name(self, obj):
        return obj.source.name

    def destination_name(self, obj):
        return obj.destination.name
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('seats','cancellation_period')
        return ()
class CustomFlightSeatManagerAdmin(admin.ModelAdmin):
    
    model = FlightSeatManager
    list_display = ('flight_name','seat','status','created_at','modified_at')
    list_filter = ('flight__name','seat','status','created_at','modified_at')
   
    search_fields = ('flight__name','seat','status','created_at','modified_at')
    ordering = ('flight__name','seat','status','created_at','modified_at')

    def flight_name(self, obj):
        return obj.flight.name

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('flight','seat')
        return ()
    
    def has_add_permission(self, request):
        return False
class CustomFlightBookinglogAdmin(admin.ModelAdmin):
    
    model = FlightBookinglog
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

    def has_add_permission(self, request):
        return False
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('flight','seat','user','status')
        return ()


admin.site.register(Country)

admin.site.register(Flight,CustomFlightAdmin)
admin.site.register(FlightSeatManager,CustomFlightSeatManagerAdmin)
admin.site.register(FlightBookinglog,CustomFlightBookinglogAdmin)