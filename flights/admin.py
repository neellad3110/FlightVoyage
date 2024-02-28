from django.contrib import admin
from .models import Country,Flight,Bookinglog
# Register your models here.

class CustomFlightAdmin(admin.ModelAdmin):
    
    model = Flight
    list_display = ('number','name','source_name','destination_name','departure_date','departure_tiime','seats')
    list_filter = ('number','name','source__name','destination__name','departure_date','departure_tiime','seats')
   
    search_fields = ('number','name','source__name','destination__name','departure_date','departure_tiime','seats',)
    ordering = ('number','name','source__name','destination__name','departure_date','departure_tiime','seats',)

    def source_name(self, obj):
        return obj.source.name

    def destination_name(self, obj):
        return obj.destination.name

admin.site.register(Country)


admin.site.register(Flight,CustomFlightAdmin)
admin.site.register(Bookinglog)