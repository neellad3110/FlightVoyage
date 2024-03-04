from django.contrib import admin
from .models import Userlog
# Register your models here.
class CustomUserlogAdmin(admin.ModelAdmin):
    
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
        if obj:
            return ('flight','seat','user')
        return ()

admin.site.register(Userlog,CustomUserlogAdmin)
